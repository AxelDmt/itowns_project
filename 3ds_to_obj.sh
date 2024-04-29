#!/bin/bash

# Ask for the folder name containing .3ds files
read -p "Enter the path of the folder containing .3ds files: " folder

# Check if the folder exists
if [ ! -d "$folder" ]; then
    echo "Folder $folder does not exist."
    exit 1
fi

# Create the "assets" folder if it doesn't already exist
mkdir -p "$folder/assets"

# Iterate over all .3ds files in the folder
for file_3ds in "$folder"/*.3ds; do
    if [ -f "$file_3ds" ]; then
        # Determine the output .obj file name
        file_obj="${file_3ds%.3ds}.obj"
        
        # Convert .3ds to .obj using assimp
        assimp export "$file_3ds" "$file_obj" -yup

        # Check if the conversion was successful
        if [ $? -eq 0 ]; then
            echo "Conversion successful: $file_3ds --> $file_obj"
            
            # Create a folder for each .obj file
            #obj_folder="$folder/assets/$(basename "${file_3ds%.3ds}")"
            #mkdir -p "$obj_folder"
            
            # Apply obj-tiler to each .obj file
            #obj-tiler -i "$file_obj" -o "$obj_folder"
        else
            echo "Conversion failed for: $file_3ds"
        fi
    fi
done

