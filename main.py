from scanner import getMiBand
from auth import MiBand3
import rabbitmq
import time
import datetime

''' ---------------------------------------------------
    This script is the main file for TCIC Mini Project
    Professor: Pedro Gonçalves
    Student: Dante Marinho
    ---------------------------------------------------
'''

# RabbitMQ object instatiation
rabbit = rabbitmq.RabbitMQ()
recent_bands_readed = {}
minutes_to_update_band_info = 3  # minutes

print('\n» Getting data from Mi Band 3...')

def sleep(t):
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{}{:02d}:{:02d}'.format('Sleeping... ', mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1

def send_to_mom(rabbit_messages):
    # Send message to RabbitMQ (MQTT)
    rabbit.connection_rabbitmq()
    for queue, msg in rabbit_messages.items():
        rabbit.queue_declare(queue)
        rabbit.send(queue, str(msg))

    rabbit.connectionClose()

def set_new_datetime_to_stored_band_mac_address(band):
    recent_bands_readed[band] = datetime.datetime.now()

def get_mi_band_infos(band):
    rabbit_messages = {}
    print('')
    mi_band = MiBand3(band, debug=True)
    mi_band.setSecurityLevel(level='medium') # medium
    mi_band.authenticate()

    # Steps
    steps_data = mi_band.get_steps()
    steps = {}
    steps['queue'] = 'steps'
    steps['mac_address'] = band
    steps['datetime'] = date_now
    steps['data'] = steps_data
    rabbit_messages['steps'] = steps
    print('\n', steps)

    # Battery
    battery_data = mi_band.get_battery_info()
    battery = {}
    battery['queue'] = 'battery'
    battery['mac_address'] = band
    battery['datetime'] = date_now
    battery['data'] = battery_data
    rabbit_messages['battery'] = battery
    print('\n', battery)

    # Heart Rate
    heart_data = mi_band.get_heart_rate_one_time()
    heart = {}
    heart['queue'] = 'heart'
    heart['mac_address'] = band
    heart['datetime'] = date_now
    heart['data'] = heart_data
    rabbit_messages['heart'] = heart
    print('\n', heart)

    mi_band.disconnect()
    send_to_mom(rabbit_messages)
    set_new_datetime_to_stored_band_mac_address(band)

while True:
    bands = getMiBand()  # Scanning for Mi Band 3 near around :: returns an array of MAC addresses

    # Loop each Mi Band 3 MAC Address and connect them to get data: "steps", "battery info", and "heart rate in real time"
    for band in bands:
        date_now = datetime.datetime.now()
        if band in recent_bands_readed:  # Verify if has recent info stored for this Mi Band
            # Verify if was get info more then 5 minutes
            time_elapsed_last_info = date_now - recent_bands_readed[band]
            if (time_elapsed_last_info.total_seconds() / 60 > minutes_to_update_band_info):
                print('» Updating Mi Band ({}) infos.'.format(band))
                get_mi_band_infos(band)
            else:
                print('» The Mi Band ({}) has already recent infos. Last date info: {}.\n'.format(band, recent_bands_readed[band].strftime("%d/%m//%Y, %H:%M:%S")))

        else:
            print('» Getting Mi Band ({}) infos.'.format(band))
            get_mi_band_infos(band)

    sleep(30)