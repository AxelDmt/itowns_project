@if "%DEBUG%" == "" @echo off
@rem ##########################################################################
@rem
@rem  3D City Database Importer/Exporter start up script for Windows
@rem  This is simply a wrapper, launching the impexp.bat CLI
@rem
@rem ##########################################################################

@rem Set local scope for the variables with windows NT shell
if "%OS%"=="Windows_NT" setlocal

set CLI_NAME=impexp.bat
set CLI_DIR=bin
set DIRNAME=%~dp0
if "%DIRNAME%" == "" set DIRNAME=.

start /min cmd /c ""%DIRNAME%%CLI_DIR%\%CLI_NAME%" gui"