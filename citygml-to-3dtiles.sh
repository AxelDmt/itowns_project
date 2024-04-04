# Save current_dir
current_dir=$(pwd)

# Go to py3dtiler repertory
cd py3dtilers

# Go to virtual environment
virtualenv -p python3 venv
. venv/bin/activate

# Install dependency
pip install -e .

echo '######################################################################################'
echo ' _____ _   _ _____ _____ _____ _____   ___________ _____ _____ _____ _   _ '
echo '/  __ \ | | |  _  |  _  /  ___|  ___| |  _  | ___ \_   _|_   _|  _  | \ | |'
echo '| /  \/ |_| | | | | | | \ `--.| |__   | | | | |_/ / | |   | | | | | |  \| |'
echo '| |   |  _  | | | | | | |`--. \  __|  | | | |  __/  | |   | | | | | | . ` |'
echo '| \__/\ | | \ \_/ | \_/ /\__/ / |___  \ \_/ / |     | |  _| |_\ \_/ / |\  |'
echo ' \____|_| |_/\___/ \___/\____/\____/   \___/\_|     \_/  \___/ \___/\_| \_/'
echo
echo 'Choose converting options from CityGML (.gml) to 3DTiles (.b3dm)'
echo
echo '######################################################################################'
echo
echo 'Welcome to this script which allows you to choose options to convert CityGML data into 3DTiles.'
echo 'This script will guide you through the process of setting up the convertion.'
echo 'Please follow the instructions of the script.'
echo 'Enter the required parameters when prompted and press ENTER to confirm.'
echo
echo '######################################################################################'    
echo                                                                                                     

# Function to prompt and read user input
read_input() {
    read -rp "$1" input
    echo "$input"
}

# Function to validate user input
validate_input() {
    local pattern=$1
    local input=$2
    [[ $input =~ $pattern ]]
}

# Prompt user for options
while true; do
    echo "Options available:"
    echo
    echo "1. Object Type"
    echo "2. Reprojection"
    echo
    echo "Press ENTER without writing anything if you chose none of the options available"
    echo
    choice=$(read_input "Enter your choice(s) (e.g., 1 for Object Type, 2 for Reprojection, 12 or 21 for both): ")

    # If user presses Enter without input, assume no options
    if [ -z "$choice" ]; then
	break
    fi

    # Validate input
    if validate_input "^[12]{1,2}$" "$choice"; then
        break
    else
        echo "Invalid input. Please enter only 1, 2 or their combinations."
    fi
done

options=""
objects=""

# Process user choice
if [[ $choice == *"1"* ]]; then
    echo
    echo "Object Types available: building, relief, water, bridge, traffic, tunnel, plant, furniture, all"
    echo "Enter multiple types separated by spaces (e.g., 'building water traffic'):"
    read -ra object_types_input

    # If 'all' is entered, populate 'objects' with all available object types
    if [[ " ${object_types_input[@]} " =~ " all " ]]; then
        objects=("building" "relief" "water" "bridge" "traffic" "tunnel" "plant" "furniture")
    else
        for object_type_input in "${object_types_input[@]}"; do
            if validate_input "^(building|relief|water|bridge|traffic|tunnel|plant|furniture)$" "$object_type_input"; then
                objects+=("$object_type_input")
            else
                echo "Invalid Object Type: $object_type_input. Skipping..."
            fi
        done
    fi
fi

if [[ $choice == *"2"* ]]; then
    while true; do
    	echo
        crs_in=$(read_input "Enter Input CRS: ")
        if validate_input "^[0-9]+$" "$crs_in"; then
            while true; do
            	echo
                crs_out=$(read_input "Enter Output CRS: ")
                if validate_input "^[0-9]+$" "$crs_out"; then
                    options+=" --crs_in $crs_in --crs_out $crs_out"
                    break 2 # Break both loops
                else
                    echo "Invalid CRS format. Please enter CRS in the format '< CRS code must be an integer higher than 0 >'."
                fi
            done
        else
            echo "Invalid CRS format. Please enter CRS in the format 'EPSG:<code>'."
        fi
    done
fi


# Convert
echo
for object in ${objects[@]}; do
    echo
    echo "Processing object type -> $object"
    citygml-tiler -i py3dtilers/CityTiler/CityTilerDBConfig.yml --type $object $options
done

# Leave the virtual environment
deactivate 

# Back to dir
cd "$current_dir"
