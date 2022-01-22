!#/bin/bash

echo "Starting setup..."

MAIN_DIR="~/field-guard"

# Create the project main directory
mkdir $MAIN_DIR
echo "Created $MAIN_DIR dir"

# Create temp directory for the images
mkdir $MAIN_DIR/temp-images
echo "Created $MAIN_DIR/temp-images dir"

# Crate scripts dir 
mkdir $MAIN_DIR/scripts
echo "Created $MAIN_DIR/scripts dir"

# Copy the relevant scripts the the main directory
cp ./run_power_supply_main.sh $MAIN_DIR/scripts
cp ./run_upload_pictures_main.sh $MAIN_DIR/scripts
echo "Copied the relevant scripts"

# Change the permissions of the scripts
sudo chmod +x $MAIN_DIR/scripts/run_power_supply_main.sh
sudo chmod +x $MAIN_DIR/scripts/run_upload_pictures_main.sh
echo "Changed the scripts poermissions"

# Setup the power supply service
sudo cp ./services/power-supply.service /etc/systemd/system/
sudo cp ./services/upload-pictures.service /etc/systemd/system/
echo "Copy the services to systemd dir"

sudo systemctl enable power-supply
echo "Enable power-supply service"

sudo systemctl enable upload-pictures
echo "Enable upload-pictures service"

