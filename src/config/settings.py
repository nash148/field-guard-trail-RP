from src.config.enums import CloudsTypes

cloud_conf = dict(
    cloud_type=CloudsTypes.DROPBOX,
    access_token='DfVUpkE0i0YAAAAAAAAAAV7YdsW0MS_8aXZ73B_AhRR85dTzTdOuzxffXM1q5QVJ'
)

gpio_conf = dict(
    power_supply_pin='5V',
    camera_pin='GPIO2',
    usb_socket_pin='GPIO3'
)

camera_conf = dict(
    time_to_shoot=1
)

files_conf = dict(
    camera_pics_path='C:\\Users\\natan\\Desktop\\images\\',
    RPi_pics_path='C:\\Users\\natan\\Desktop\\Projects\\field-guard\\repositories\\field-guard-trail-RP\\images\\',
    remote_pics_path='/field-guard/events/'
)
