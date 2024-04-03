3D City Database Importer/Exporter

Version 5.4.0 (2023-09-21)

  This software is free software and is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License. 


0. Index
--------

1. License
2. Copyright
3. About
4. System requirements
5. (Un)Installation
6. Running the application
7. Documentation
8. Cooperation partners and supporters
9. Active Developers
10. Contact
11. Websites
12. Disclaimer


1. License
----------

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this software except in compliance with the License.
You may obtain a copy of the License at
 
    http://www.apache.org/licenses/LICENSE-2.0


2. Copyright
------------

(C) 2013-2023
Chair of Geoinformatics
Technical University of Munich, Germany
https://www.lrg.tum.de/gis


3. About
--------

The 3D City Database Importer/Exporter is a Java based client for
the 3D City Database version 4.4.x. It allows for high-performance 
loading and extracting 3D city model data.

* Support for CityGML 2.0 and 1.0
* Support for CityJSON 1.0
* Support for CityGML Application Domain Extensions (ADEs) through
  software extensions
* Support for PostgreSQL/PostGIS and Oracle Spatial
* Reading/writing CityGML instance documents of arbitrary file size
* Export of KML/COLLADA/glTF models including tiling schemas for 
  visualization and interactive exploration of large city models
  in Digital Earth Browsers, 3D GIS, and computer graphics software
* Generic KML information balloons
* Export of thematic object data into tables. Supported data formats are
  CSV and Microsoft Excel
* Resolving and preservation of forward and backwards XLinks in
  CityGML datasets
* Full support of 3D Coordinate Reference Systems (CRS) and 3D
  coordinate transformations; support for user-defined CRS
* Coordinate transformations for CityGML/CityJSON exports
* Map window for graphical selection of bounding boxes
* Validation of CityGML/CityJSON instance documents
* Multithreaded programming facilitating high-performance data processing

The 3D City Database Importer/Exporter comes with both a Graphical
User Interface (GUI) and a Command Line Interface (CLI). The CLI 
allows for employing the tool in batch processing workflows and 
third party applications.


4. System requirements
----------------------

* Java JRE or JDK >= 8
* 3D City Database version 4.4.x on
  - PostgreSQL DBMS >= 11 with PostGIS extension >= 2.5
  - Oracle Spatial DBMS >= 19c
  - PolarDB for PostgresSQL >= 1.1 with Ganos >= 4.6

The 3D City Database Importer/Exporter can be run on any platform 
providing appropriate Java support. It has been tested on the 
following platforms:
  - Microsoft Windows 7, 8, 10, 11
  - Apple Mac OS X and macOS
  - Ubuntu 9 - 22


5. (Un)Installation
-------------------

It is recommended to use the universal installer to setup the
3D City Database Importer/Exporter application on your local computer.
The universal installer will guide you through the steps of the
installation process. Afterwards, you can immediately run the application 
(see next section).

When you successfully install the 3D City Database Importer/Exporter,
an uninstaller is automatically generated in the "uninstaller" subfolder
of the installation directory. Please use this uninstaller in order to remove
the 3D City Database Importer/Exporter application files from your
computer. Alternatively, you can simply delete the entire installation
directory.


6. Running the application
--------------------------

For running the 3D City Database Importer/Exporter use one of the
following two options:

a) Use the start scripts to launch the application with a graphical user
   interface. The start scripts are located in the installation directory.
   During setup, you can additionally choose to create shortcuts for the
   start scripts on your desktop and in the start menu of your preferred OS.

   Please execute the start script suitable for your platform:
   - 3DCityDB-Importer-Exporter.bat   (Microsoft Windows family)
   - 3DCityDB-Importer-Exporter       (UNIX/Linux family, macOS)

   On many platforms, double-clicking the start script or its shortcut
   runs the 3D City Database Importer/Exporter.

   For some UNIX/Linux distributions, you will have to run the start
   script from within a shell environment. Please open your favorite shell
   and first check whether execution rights are correctly set for the
   start script.

   Change to the installation directory and enter the following to make
   the start script executable for the owner of the file:

       chmod u+x 3DCityDB-Importer-Exporter

   Afterwards, simply run the start script by the following command:

       ./3DCityDB-Importer-Exporter

b) The 3D City Database Importer/Exporter also offers a
   Command Line Interface (CLI). The CLI can be used to run single operations
   like a CityGML import or export and allows for easily embedding the tool
   in batch processing workflows and third party applications.

   The CLI scripts are located in the "bin" subfolder of the installation
   directory. Open a shell, change to the "bin" folder and use the CLI
   script suitable for your platform:
   - impexp.bat   (Microsoft Windows family)
   - impexp       (UNIX/Linux family, macOS)

   To show the help message and all available subcommands, simply type the
   following command:

       impexp --help

   PLEASE NOTE:
   The CLI scripts set the initial heap size of the Java Virtual Machine (JVM)
   to 1GB using the -Xms parameter of the JVM. This value has been chosen to
   be reasonable for most scenarios. Please edit the CLI scripts in case you
   need to adapt the default value. You can also use the environment variables
   JAVA_OPTS and IMPEXP_OPTS to pass JVM options to the CLI scripts.


7. Documentation
----------------------------
A complete and comprehensive documentation on the 3D City Database
and the 3D City Database Importer/Exporter is available online at:

https://3dcitydb-docs.readthedocs.io/en/version-2023.0/

  
8. Cooperation partners and supporters
--------------------------------------

The 3D City Database Importer/Exporter v5.4.0 has been developed by
and with the support from the following cooperation partners:

* Chair of Geoinformatics, Technical University of Munich
  https://www.lrg.tum.de/gis/
* Virtual City Systems, Berlin
  https://vc.systems/
* M.O.S.S. Computer Grafik Systeme GmbH, Taufkirchen
  http://www.moss.de/
  
   
9. Active Developers
--------------------

Claus Nagel <cnagel@vc.systems>
Zhihang Yao <zyao@vc.systems>
Luca Casagrande <lcasagrande@moss.de>
Felix Kunde <felix-kunde@gmx.de>
Son H. Nguyen <son.nguyen@tum.de>
Thomas H. Kolbe <thomas.kolbe@tum.de>

Version 5.4.0 is based on earlier versions of the
3D City Database Importer/Exporter. Please refer to the 3D City Database
documentation for the list of all contributors to previous versions. 


10. Contact
----------

cnagel@vc.systems
thomas.kolbe@tum.de


11. Websites
------------

Official 3D City Database website: 
https://www.3dcitydb.org

Related websites:
https://github.com/3dcitydb
https://github.com/tum-gis/3dcitydb-docker-postgis
https://www.lrg.tum.de/gis
http://www.citygml.org
http://www.citygmlwiki.org
http://www.opengeospatial.org/standards/citygml


12. Disclaimer
--------------

THIS SOFTWARE IS PROVIDED BY THE CHAIR OF GEOINFORMATION FROM TU MUNICH
(TUMGI) "AS IS" AND "WITH ALL FAULTS." 
TUMGI MAKES NO REPRESENTATIONS OR WARRANTIES OF ANY KIND CONCERNING THE 
QUALITY, SAFETY OR SUITABILITY OF THE SOFTWARE, EITHER EXPRESSED OR 
IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF 
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, OR NON-INFRINGEMENT.

TUMGI MAKES NO REPRESENTATIONS OR WARRANTIES AS TO THE TRUTH, ACCURACY OR 
COMPLETENESS OF ANY STATEMENTS, INFORMATION OR MATERIALS CONCERNING THE 
SOFTWARE THAT IS CONTAINED ON AND WITHIN ANY OF THE WEBSITES OWNED AND 
OPERATED BY TUMGI.

IN NO EVENT WILL TUMGI BE LIABLE FOR ANY INDIRECT, PUNITIVE, SPECIAL, 
INCIDENTAL OR CONSEQUENTIAL DAMAGES HOWEVER THEY MAY ARISE AND EVEN IF 
TUMGI HAVE BEEN PREVIOUSLY ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.