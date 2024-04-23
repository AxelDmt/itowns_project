#!/bin/bash

# Demander le nom du dossier contenant les fichiers .3ds
read -p "Entrez le chemin du dossier contenant les fichiers .3ds : " dossier

# Vérifie si le dossier existe
if [ ! -d "$dossier" ]; then
    echo "Le dossier $dossier n'existe pas."
    exit 1
fi

# Créer le dossier "assets" s'il n'existe pas déjà
mkdir -p "$dossier/assets"

# Parcourir tous les fichiers .3ds dans le dossier
for fichier_3ds in "$dossier"/*.3ds; do
    if [ -f "$fichier_3ds" ]; then
        # Déterminer le nom du fichier .obj de sortie
        fichier_obj="${fichier_3ds%.3ds}.obj"
        
        # Conversion .3ds en .obj avec assimp
        assimp export "$fichier_3ds" "$fichier_obj" -yup

        # Vérifier si la conversion a réussi
        if [ $? -eq 0 ]; then
            echo "Conversion réussie: $fichier_3ds --> $fichier_obj"
            
            # Créer un dossier pour chaque fichier .obj
            #dossier_obj="$dossier/assets/$(basename "${fichier_3ds%.3ds}")"
            #mkdir -p "$dossier_obj"
            
            # Appliquer obj-tiler à chaque fichier .obj
            #obj-tiler -i "$fichier_obj" -o "$dossier_obj"
        else
            echo "La conversion a échoué pour : $fichier_3ds"
        fi
    fi
done

