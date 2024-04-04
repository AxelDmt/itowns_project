# Itowns - CityGML to 3DTiles pipeline

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
