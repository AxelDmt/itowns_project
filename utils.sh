##Install
java -jar 3DCityDB-Importer-Exporter-{version}-Setup.jar -console
java -jar 3DCityDB-Importer-Exporter-5.4.0-Setup.jar -console

##Import (cd 3DCityDB-Importer-Exporter-5.4.0/bin/) or (1)
impexp import -H <host> -d <database> -u <username> -p <password> -o <import_mode> --import-log=<import_log_file> --duplicate-log=<duplicate_log_file> --input-encoding=<encoding> --worker-threads=<threads> <file.gml>
./impexp import -H localhost -d my3dcitydb -u postgres -p postgres -o delete /var/data/store-echange/ALavenant/Marseille/AU03.IGN.GML 


##Clean DB
#!/bin/bash

# Configuration de la base de données
DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=my3dcitydb
DB_HOST=localhost
DB_PORT=5432


# Connexion à la base de données et récupération de la liste des tables
TABLES=$(PGPASSWORD=$DB_PASSWORD psql -U "$DB_USER" -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -t -c "\dt" | cut -d '|' -f 2 | sed '/^\s*$/d')

# Nettoyage des tables
for TABLE in $TABLES; do
    PGPASSWORD=$DB_PASSWORD psql -U "$DB_USER" -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "TRUNCATE TABLE \"$TABLE\" CASCADE;"
done

echo "Nettoyage terminé."

#(1)To use impexp
export PATH=/home/ADumont/3DCityDB-Importer-Exporter/bin:$PATH


sudo apt-get install -y libpq-dev       
sudo apt-get install python3 python3-dev
sudo apt-get install virtualenv git

git clone https://github.com/VCityTeam/py3dtilers
cd py3dtilers
virtualenv -p python3 venv
. venv/bin/activate

#Once in the VENV
pip install -e .
citygml-tiler -i py3dtilers/CityTiler/CityTilerDBConfig.yml

# Installer PostgreSQL et PostGIS si ce n'est pas déjà fait
sudo apt-get update
sudo apt-get install -y postgresql postgis


PG_HOST: localhost
PG_PORT: 5432
PG_NAME: my3dcitydb
PG_USER: postgres
PG_PASSWORD: postgres
