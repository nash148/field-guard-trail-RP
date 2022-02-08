# field-guard-trail-RP - v0

## Description
This program runs over RPi.

The program takes photos from the connected camera for N seconds,
and uploads them to the cloud (Dropbox for now).

## Usage

Configure the relevant parameters in ```/src/config/settings.json``` file, and run ```/scripts/setup.sh```.

**Note: There is no configuration validation - the program will crash in case of wrong configuration.**
