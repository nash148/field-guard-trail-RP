#!/bin/bash

while ! ping -c 1 -W 1 8.8.8.8; do
	echo "Waiting for internet"
	sleep 1
done

#sudo systemctl start mnt-volume.automount

cd /home/pi/clones/field-guard-trail-RP
sudo python ./src/upload_pictures_main.py > /dev/tty1
