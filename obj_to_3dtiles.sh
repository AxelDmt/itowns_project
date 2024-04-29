#!/bin/bash

# Path to .obj directory
input_dir="py3dtilers/output_/"

# Output path
output_dir="py3dtilers/output_/output_dir"

# Create dir if not existing already
mkdir -p "$output_dir"

# Go to each .obj files
for obj_file in "$input_dir"/*.obj; do
    # Verif if there is .obj files
    if [ -e "$obj_file" ]; then
        # Create dir for each .obj files
        obj_dir="${obj_file%.*}"
        mkdir -p "$obj_dir"

        # Execute obj-tiler for current .obj
        obj-tiler -i "$obj_file" -o "$obj_dir" --crs_in 2154 --crs_out 4978

        # Move in output dir
        mv "$obj_dir" "$output_dir"
        
        # Delete the .obj file
        rm "$obj_file"
        
    fi
done

# Check if the output directory exists, if not, create it
if [ ! -d "$output_dir" ]; then
  mkdir -p "$output_dir"
fi

# Traverse all subdirectories of the tilesets directory
for tileset_folder in "$tilesets_directory"/*; do
  if [ -d "$tileset_folder" ]; then
    # Build the list of tilesets paths
    tileset_list+=("$tileset_folder")
  fi
done

# Check if there are at least two tilesets to merge
if [ ${#tileset_list[@]} -ge 2 ]; then
  # Merge the tilesets into a single file
  tileset-merger -i "${tileset_list[@]}" --output_dir "$output_dir"
else
  echo "There are not enough tilesets to merge."
fi

# Delete useless dir
rm "$output_dir"
