import psycopg2
import numpy as np
from pywavefront import Wavefront
from shapely.geometry import Point, MultiPoint
from binascii import a2b_hex
from shapely.wkb import loads as wkb_loads

# Connecting to the database
conn = psycopg2.connect(
    dbname="my3dcitydb",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

def calculate_centroid_from_obj(file_path):
    """
    Calculate centroid from a Wavefront .obj file.
    :param file_path: Path to the .obj file.
    :return: Centroid coordinates as a list [x, y, z].
    """
    vertices = []
    faces = []
    total_vertices = 0
    centroid = [0, 0, 0]

    # Open the .obj file and read the data
    with open(file_path, 'r') as obj_file:
        for line in obj_file:
            if line.startswith('v '):  # Read vertices
                vertex = list(map(float, line.strip().split()[1:]))
                vertices.append(vertex)
                total_vertices += 1
            elif line.startswith('f '):  # Read faces
                face = line.strip().split()[1:]
                face_indices = []
                for vertex_info in face:
                    # Ignore additional information and take only the vertex index
                    vertex_index = int(vertex_info.split('/')[0]) - 1
                    face_indices.append(vertex_index)
                faces.append(face_indices)

    # Calculate centroid considering faces
    for face in faces:
        # Calculate centroid of each face using the average of its vertices
        face_centroid = [0, 0, 0]
        for vertex_index in face:
            vertex = vertices[vertex_index]
            face_centroid[0] += vertex[0]
            face_centroid[1] += vertex[1]
            face_centroid[2] += vertex[2]
        face_centroid[0] /= len(face)
        face_centroid[1] /= len(face)
        face_centroid[2] /= len(face)

        # Add face's contribution to the global centroid
        centroid[0] += face_centroid[0]
        centroid[1] += face_centroid[1]
        centroid[2] += face_centroid[2]

    centroid[0] /= len(faces)
    centroid[1] /= len(faces)
    centroid[2] /= len(faces)

    return centroid


def apply_transfo_to_point(matrix, point_obj, point_reel):
    """
    Apply transformation to a 3D object's local referential to get in a global referential.
    :param matrix: a 4x4 transformation matrix.
    :param point_obj: coordinates from the 3D object's local referential.
    :param point_reel: coordinates of the 3D objects in the global referential (in WKB).
    :return: Transformed point coordinates as a tuple (x, y, z).
    """
    
    # Define the rotation matrix for 90 degrees around the X axis
    rotation_x_90 = np.array([[1, 0, 0, 0],
                               [0, 0, -1, 0],
                               [0, 1, 0, 0],
                               [0, 0, 0, 1]])
                               
    matrix_4x4 = np.array(matrix).reshape((4, 4))
    matrix_4x4 = np.dot(matrix_4x4, rotation_x_90)
                               
    point_homogeneous = np.array([[point_obj[0]], [point_obj[1]], [point_obj[2]], [1.0]])
    transformed_point = np.dot(matrix_4x4, point_homogeneous)

    geom = wkb_loads(a2b_hex(point_reel))
    x, y, z = geom.x, geom.y, geom.z

    res = (transformed_point[0][0] + x, transformed_point[1][0] + y, transformed_point[2][0] + z)

    return res
 
def transform_obj_file(input_file, output_file, matrix, point_reel):
    """
    Transform a 3D object (.obj) file based on a given transformation matrix and real-world coordinates.

    :param input_file: The path to the input 3D object file.
    :param output_file: The path to save the transformed 3D object file.
    :param matrix: A 4x4 transformation matrix.
    :param point_reel: Coordinates of the 3D object in the global referential (in WKB).
    :return: None
    """
    with open(input_file, 'r') as f:
        lines = f.readlines()

    transformed_points = []

    for line in lines:
        if line.startswith('v '):
            vertices = line.split()[1:]
            point_obj = [float(coord) for coord in vertices]
            # Assuming point_reel is available or can be calculated somehow
            transformed_point = apply_transfo_to_point(matrix, point_obj, point_reel)
            transformed_points.append(transformed_point)
        else:
            # For lines other than vertex lines, just keep them as is
            transformed_points.append(line)

    with open(output_file, 'w') as f:
        for item in transformed_points:
            if isinstance(item, tuple):
                f.write("v " + " ".join(str(coord) for coord in item) + "\n")
            else:
                f.write(item)
    
def string_to_flat_list(input_string):
    """
    Convert a string of space-separated numerical values into a flat list of floats.

    :param input_string: A string containing space-separated numerical values.
    :return: A flat list of floating-point numbers.
    """
    values = input_string.split()  # Split the input string into individual values
    return [float(value) for value in values]  # Convert each value to a float and return as a list



try:
    # Select all IDs of implicit geometries present in city_furniture
    cursor.execute("SELECT id, lod2_implicit_rep_id, lod2_implicit_transformation, lod2_implicit_ref_point FROM building_installation WHERE lod2_implicit_rep_id IS NOT NULL")
    implicit_ids = cursor.fetchall()

    # Create a dictionary to store the associations between id and lod2_implicit_rep_id
    id_to_implicit_id = {row[0]: (row[1], row[2], row[3], (0.0, 0.0, 0.0)) for row in implicit_ids}

    # Select matches between IDs and references by replacing .3ds with .obj
    cursor.execute("SELECT building_installation.lod2_implicit_rep_id, REPLACE(implicit_geometry.reference_to_library, '.3ds', '.obj') FROM building_installation INNER JOIN implicit_geometry ON building_installation.lod2_implicit_rep_id = implicit_geometry.id")
    id_references = cursor.fetchall()

    # Create a Python dictionary with braces to store the links between IDs and references
    id_to_reference = {id_ref[0]: id_ref[1] for id_ref in id_references}

    '''# Iterate through the dictionary to load each .obj file, calculate the centroid, and add it to the dictionary
    for implicit_id, reference in id_to_reference.items():
        path = "assets/implicit/3ds_obj/" + reference
        # Calculate the centroid
        centroid = calculate_centroid_from_obj(path)
        # Add centroid coordinates to the dictionary
        id_to_reference[implicit_id] = (reference, (centroid[0], centroid[1], centroid[2]))'''

    # Display the created dictionary
    print("\nDictionary linking IDs to references by replacing .3ds with .obj:")
    print(id_to_reference)
    
    for id, (implicit_id, matrix, point_reel, transfo) in id_to_implicit_id.items():
        input_file = id_to_reference[implicit_id]
        road_to_input_file = "assets/implicit/3ds_obj/" + input_file
        index_point = input_file.rfind(".")
        name_without_obj = input_file[:index_point]
        output_file = "py3dtilers/output_building/" + str(id) + "_" + name_without_obj  + ".obj"
        matrice = string_to_flat_list(matrix)
        transform_obj_file(road_to_input_file, output_file, matrice, point_reel)
    #print(id_to_implicit_id) 

except psycopg2.Error as e:
    print("Error executing PostgreSQL query:", e)

finally:
    # Close the connection to the database
    cursor.close()
    conn.close()
