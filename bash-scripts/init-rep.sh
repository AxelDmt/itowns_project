#Back to lobby
cd ..

echo
echo '##################################### Apt installs #######################################################'

# Install useful packages
sudo apt-get install -y libpq-dev       
sudo apt-get install python3 python3-dev
sudo apt-get install virtualenv git
sudo apt-get install -y postgresql postgis

echo
echo '##################################### Clone py3dtilers ##################################################'

# Clone py3dtilers
#git clone https://github.com/VCityTeam/py3dtilers

echo
echo '##################################### Download 3dcitydb #################################################'

# Download 3dcitydb
wget https://github.com/3dcitydb/3dcitydb/releases/download/v4.4.0/3dcitydb-4.4.0.zip

# Verif download
if [ $? -eq 0 ]; then
    echo "Download successful."
else
    echo "Error while dowloading. Check URL or internet connection."
    exit 1
fi

# Extract
unzip 3dcitydb-4.4.0.zip

# Verif extract
if [ $? -eq 0 ]; then
    echo "Extraction successful."
else
    echo "Error while extracting ZIP file."
    exit 1
fi

# Cleaning zip
rm 3dcitydb-4.4.0.zip

echo "3dcitydb succesfuly download."

echo
echo '####################################### Download 3dcitydb impexp #########################################'
# Download impexp 3dcitydb
wget https://github.com/3dcitydb/importer-exporter/releases/download/v5.4.0/3DCityDB-Importer-Exporter-5.4.0.zip

# Verif download
if [ $? -eq 0 ]; then
    echo "Download successful."
else
    echo "Error while dowloading. Check URL or internet connection."
    exit 1
fi

# Extract
unzip 3DCityDB-Importer-Exporter-5.4.0.zip

# Verif extract
if [ $? -eq 0 ]; then
    echo "Extraction successful."
else
    echo "Error while extracting ZIP file."
    exit 1
fi

# Cleaning zip
rm 3DCityDB-Importer-Exporter-5.4.0.zip

echo "3dcitydb importer/exporter succesfuly download."



