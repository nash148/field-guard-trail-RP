from src.config.enums import CloudsTypes

cloud_conf = dict(
    cloud_type=CloudsTypes.DROPBOX,
    access_token='DfVUpkE0i0YAAAAAAAAAAV7YdsW0MS_8aXZ73B_AhRR85dTzTdOuzxffXM1q5QVJ'
)

gpio_conf = dict(
    power_supply_pin='GPIO4',
    camera_pin='GPIO22',
    usb_socket_pin='GPIO23',
    reset_camera_pin='GPIO24',
)

debug_gpio_conf = dict(
    startup_pin='GPIO5',
    file_transfer_pin='GPIO6',
    cloud_upload_pin='GPIO26'
)

camera_conf = dict(
    time_to_shoot=1
)

files_conf = dict(
    camera_pics_path='/mnt/volume/DCIM/100MEDIA/',
    RPi_pics_path='/home/pi/field-guard/temp-images/',
    remote_pics_path='/field-guard/events/',
    mount_point_path='/mnt/volume'
)
