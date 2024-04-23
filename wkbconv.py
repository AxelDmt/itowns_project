import psycopg2
from shapely.wkb import loads
from pyproj import Proj, transform
import json
from pywavefront import Wavefront


# Connexion à la base de données
conn = psycopg2.connect(
    dbname="my3dcitydb",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Définir la projection source (2154) et la projection cible (4326)
src_proj = Proj(init='epsg:2154')
dst_proj = Proj(init='epsg:4326')

# Sélectionner les données de la table city_furniture excluant les valeurs nulles
cursor.execute("SELECT lod2_implicit_ref_point, lod2_implicit_rep_id, lod2_implicit_transformation FROM city_furniture WHERE lod2_implicit_ref_point IS NOT NULL")
rows = cursor.fetchall()

# Tableau pour stocker les coordonnées converties, les IDs et les altitudes
converted_data = []

# Parcourir les résultats
for row in rows:
    hex_location = row[0]  # Récupérer la colonne de l'attribut lod2_implicit_ref_point
    point = loads(hex_location, hex=True)  # Convertir le WKB en objet géométrique Shapely
    longitude = point.x
    latitude = point.y
    altitude = point.z
    lod2_implicit_rep_id = row[1]  # Récupérer l'ID lod2_implicit_rep_id
    
    # Convertir les coordonnées
    longitude_4326, latitude_4326 = transform(src_proj, dst_proj, point.x, point.y)

    # Ajouter les coordonnées converties, l'ID et l'altitude au tableau
    converted_data.append((longitude_4326, latitude_4326, lod2_implicit_rep_id, point.z))

# Récupérer les correspondances entre lod2_implicit_rep_id et ID de implicit_geometry
cursor.execute("SELECT city_furniture.lod2_implicit_rep_id, implicit_geometry.id FROM city_furniture INNER JOIN implicit_geometry ON city_furniture.lod2_implicit_rep_id = implicit_geometry.id")
id_mappings = cursor.fetchall()

# Récupérer les noms des fichiers .3ds
file_names = {}
for mapping in id_mappings:
    lod2_implicit_rep_id, implicit_geometry_id = mapping
    cursor.execute("SELECT reference_to_library FROM implicit_geometry WHERE id = %s", (implicit_geometry_id,))
    file_name = cursor.fetchone()[0]
    # Remplacer l'extension .3ds par .obj dans le nom de fichier
    file_name = file_name.replace(".3ds", ".obj")
    file_names[lod2_implicit_rep_id] = file_name


print(file_names.get(2))
print(file_names.get(5))
# Afficher les données converties avec les noms de fichier .3ds
print("Données converties avec noms de fichiers .3ds :")
for data in converted_data:
    print("Longitude:", data[0])
    print("Latitude:", data[1])
    print("Altitude:", data[3])
    print("ID lod2_implicit_rep_id:", data[2])
    print("Nom du fichier .3ds:", file_names.get(data[2]))
    print("")
