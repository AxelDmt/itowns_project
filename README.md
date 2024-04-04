# iTowns pipelines to convert CityGML data from 3DCityDB into 3DTiles

## Initialize repository

```bash
git clone https://github.com/AxelDmt/itowns_project.git
cd itowns_project
./init-rep.sh
```

## Initialize 3DCityDB on PostgreSQL

Go to ../3dcitydb-4.4.0/postgresql/ShellScripts/Unix/CONNECTION_DETAILS.sh and change the content of the file to this : 

```bash
#!/bin/bash
# Provide your database details here ------------------------------------------
export PGBIN=/etc/postgresql/14/main
export PGHOST=localhost
export PGPORT=5432
export CITYDB=my3dcitydb
export PGUSER=postgres
#------------------------------------------------------------------------------
```

When this is done, execute [init-3dcitydb.sh](http://init-3dcitydb.sh) :

```bash
./init-3dcitydb.sh
```

If everythings runs the right way you should see this :

```bash
######################################################################################

 _______   ___ _ _        ___  ___ 
|__ /   \ / __(_) |_ _  _|   \| _ )
 |_ \ |) | (__| |  _| || | |) | _ \
|___/___/ \___|_|\__|\_, |___/|___/
                     |__/          

3D City Database - The Open Source CityGML Database

######################################################################################

Welcome to the 3DCityDB Setup Script. This script will guide you through the process
of setting up a 3DCityDB instance. Please follow the instructions of the script.
Enter the required parameters when prompted and press ENTER to confirm.
Just press ENTER to use the default values.

Documentation and help:
   3DCityDB website:    https://www.3dcitydb.org
   3DCityDB on GitHub:  https://github.com/3dcitydb

Having problems or need support?
   Please file an issue here:
   https://github.com/3dcitydb/3dcitydb/issues

######################################################################################

Please enter a valid SRID (e.g., EPSG code of the CRS to be used).
(SRID must be an integer greater than zero): 2154

Please enter the EPSG code of the height system (use 0 if unknown or '2154' is already 3D).
(default HEIGHT_EPSG=0): 

Please enter the corresponding gml:srsName to be used in GML exports.
(default GMLSRSNAME=urn:ogc:def:crs:EPSG::2154): 

Connecting to "postgres@localhost:5432/my3dcitydb" ...
Password for user postgres: 
```

## Start local servers

### Starting itowns :

```bash
cd itowns-starter-webpack
npm install
npm start --cors
```

### Starting data server for itowns :

```bash
npm install -g http-server
http-server --cors -p 8000
```

## Importing CityGML data in your 3DCityDB

```bash
./import.sh
```

If everythings runs the right way (and enter ‘2’) you should see this :

```bash
######################################################################################
 ________  _________ ___________ _____ 
|_   _|  \/  || ___ \  _  | ___ \_   _|
  | | | .  . || |_/ / | | | |_/ / | |  
  | | | |\/| ||  __/| | | |    /  | |  
 _| |_| |  | || |   \ \_/ / |\ \  | |  
 \___/\_|  |_/\_|    \___/\_| \_| \_/  

3D City Database - Import CityGML data

######################################################################################

Welcome to this script which allows you to import CityGML data to a postgreSQL 3DCityDB.
This script will guide you through the process of setting up the import.
Please follow the instructions of the script.
Enter the required parameters when prompted and press ENTER to confirm.

######################################################################################

Select import mode:
1. Import a single CityGML file
2. Import all CityGML files in a directory
Enter your choice (1 or 2): 2
Username: 
Password: 
Host: host
Database name: 
Import Mode (import_all/skip/delete/terminate): 
Path to directory containing CityGML files (path/to/directory):
```

## Converting CityGML data into 3DTiles

```bash
./citygml-to-3dtiles.sh
```

If everythings runs the right way (and enter ‘21’ or ‘12’) you should see this :

```bash
######################################################################################
 _____ _   _ _____ _____ _____ _____   ___________ _____ _____ _____ _   _ 
/  __ \ | | |  _  |  _  /  ___|  ___| |  _  | ___ \_   _|_   _|  _  | \ | |
| /  \/ |_| | | | | | | \ `--.| |__   | | | | |_/ / | |   | | | | | |  \| |
| |   |  _  | | | | | | |`--. \  __|  | | | |  __/  | |   | | | | | | . ` |
| \__/\ | | \ \_/ | \_/ /\__/ / |___  \ \_/ / |     | |  _| |_\ \_/ / |\  |
 \____|_| |_/\___/ \___/\____/\____/   \___/\_|     \_/  \___/ \___/\_| \_/

Choose converting options from CityGML (.gml) to 3DTiles (.b3dm)

######################################################################################

Welcome to this script which allows you to choose options to convert CityGML data into 3DTiles.
This script will guide you through the process of setting up the convertion.
Please follow the instructions of the script.
Enter the required parameters when prompted and press ENTER to confirm.

######################################################################################

Options available:

1. Object Type
2. Reprojection

Press ENTER without writing anything if you chose none of the options available

Enter your choice(s) (e.g., 1 for Object Type, 2 for Reprojection, 12 or 21 for both): 21

Object Types available: building, relief, water, bridge, traffic, tunnel, plant, furniture, all
Enter multiple types separated by spaces (e.g., 'building water traffic'):
relief

Enter Input CRS: 2154

Enter Output CRS: 4978
```

## Use iTowns

To use iTowns and visualize your converted data, go to : http://localhost:8080/
