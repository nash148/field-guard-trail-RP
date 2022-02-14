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
echo "Changed the scripts permissions"

sudo chown -R pi.pi /home/pi/field-guard/
echo "Change own to pi.pi"

sudo mkdir /mnt/volume
echo "Created mnt folder"

# Setup services
sudo cp ./services/power-supply.service /etc/systemd/system/
sudo cp ./services/upload-pictures.service /etc/systemd/system/
echo "Copy the services to systemd dir"

sudo systemctl enable power-supply.service
echo "Enable power-supply service"

sudo systemctl enable upload-pictures.service
echo "Enable upload-pictures service"


