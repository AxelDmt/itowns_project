#!/bin/bash

# Save current_dir
current_dir=$(pwd)

# Welcome message
echo '######################################################################################'
echo ' ________  _________ ___________ _____ '
echo '|_   _|  \/  || ___ \  _  | ___ \_   _|'
echo '  | | | .  . || |_/ / | | | |_/ / | |  '
echo '  | | | |\/| ||  __/| | | |    /  | |  '
echo ' _| |_| |  | || |   \ \_/ / |\ \  | |  '
echo ' \___/\_|  |_/\_|    \___/\_| \_| \_/  '
echo
echo '3D City Database - Import CityGML data'
echo
echo '######################################################################################'
echo
echo 'Welcome to this script which allows you to import CityGML data to a postgreSQL 3DCityDB.'
echo 'This script will guide you through the process of setting up the import.'
echo 'Please follow the instructions of the script.'
echo 'Enter the required parameters when prompted and press ENTER to confirm.'
echo
echo '######################################################################################'    
echo                                   
# Ask import mode
echo "Select import mode:"
echo "1. Import a single CityGML file"
echo "2. Import all CityGML files in a directory"
read -p "Enter your choice (1 or 2): " import_choice

if [ "$import_choice" == "1" ]; then
    # Ask import informations for single file
    read -p "Username: " username
    read -sp "Password: " password
    echo
    read -p "Host: " host
    read -p "Database name: " database
    read -p "Import Mode (import_all/skip/delete/terminate): " import_mode
    read -p "Path to file (path/to/file/city.gml): " file_path

    # Access to impexp command
    cd 3DCityDB-Importer-Exporter-5.4.0/bin
    # Execute import
    ./impexp import -H "$host" -d "$database" -u "$username" -p "$password" -o "$import_mode" "$file_path"
    # Back to dir
    cd "$current_dir"

elif [ "$import_choice" == "2" ]; then
    # Ask import informations for directory
    read -p "Username: " username
    read -sp "Password: " password
    echo
    read -p "Host: " host
    read -p "Database name: " database
    read -p "Import Mode (import_all/skip/delete/terminate): " import_mode
    read -p "Path to directory containing CityGML files (path/to/directory): " dir_path

    # Access to impexp command
    cd 3DCityDB-Importer-Exporter-5.4.0/bin

    # Execute import for all files in directory
    for file in "$dir_path"/*.GML; do
    	./impexp import -H "$host" -d "$database" -u "$username" -p "$password" -o "$import_mode" "$file"
    	echo
    	echo '######################################################################################'   
    	echo 
    	echo "$file successfuly imported."
    	echo
    	echo '######################################################################################'   
    	echo 
    done
    # Back to dir
    cd "$current_dir"
else
    echo "Invalid choice. Exiting."
    exit 1
fi
