#!/bin/bash

echo "Starting setup..."

MAIN_DIR="~/field-guard"

# pip install
echo "pip install..."
sudo pip3 install -r ../requirenments.txt

# Create the project main directory
mkdir /home/pi/field-guard
echo "Created $MAIN_DIR dir"

# Create temp directory for the images
mkdir /home/pi/field-guard/temp-images
echo "Created $MAIN_DIR/temp-images dir"

# Crate scripts dir 
mkdir /home/pi/field-guard/scripts
echo "Created $MAIN_DIR/scripts dir"

# Copy the relevant scripts the the main directory
cp ./run_power_supply_main.sh /home/pi/field-guard/scripts
cp ./run_upload_pictures_main.sh /home/pi/field-guard/scripts
echo "Copied the relevant scripts"

# Change the permissions of the scripts
sudo chmod +x /home/pi/field-guard/scripts/run_power_supply_main.sh
sudo chmod +x /home/pi/field-guard/scripts/run_upload_pictures_main.sh
echo "Changed the scripts poermissions"

sudo mkdir /mnt/volume
echo "Created mnt folder"

# Setup services
sudo cp ./services/power-supply.service /etc/systemd/system/
sudo cp ./services/upload-pictures.service /etc/systemd/system/
sudo cp ./services/mnt-volume.automount /etc/systemd/system/
sudo cp ./services/mnt-volume.mount /etc/systemd/system/

echo "Copy the services to systemd dir"

echo "Change servics permissions"
sudo chmod +x /etc/systemd/system/power-supply.service
sudo chmod +x /etc/systemd/system/upload-pictures.service

sudo systemctl enable power-supply
echo "Enable power-supply service"

sudo systemctl enable upload-pictures
echo "Enable upload-pictures service"

sudo systemctl enable --now  mnt-volume.mount mnt-volume.automount
echo "Enable auto mount services"


