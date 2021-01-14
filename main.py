from scanner import getMiBand
from auth import MiBand3
import rabbitmq
import time

''' ---------------------------------------------------
    This script- is the main file for TCIC Mini Project
    Professor: Pedro Gonçalves
    Student: Dante Marinho
    ---------------------------------------------------
'''

# Object instatiation
rabbit = rabbitmq.RabbitMQ()

# Scanning for Mi Band 3 near aroud :: returns an array of MAC addresses
bands = getMiBand()

print('\n» Getting data from Mi Band 3...')

def sleep(t):
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1

while True:
    # Loop each Mi Band 3 MAC Address and connect them to get data: "steps", "battery info", and "heart rate in real time"
    for band in bands:
        rabbit_messages = {}

        print('Mi Band with MAC Address ' + band + '\n')
        mi_band = MiBand3(band, debug=True)
        mi_band.setSecurityLevel(level='medium') # medium
        mi_band.authenticate()

        # Steps
        steps_data = mi_band.get_steps()
        steps = {}
        steps['queue'] = 'steps'
        steps['mac_address'] = band
        steps['data'] = steps_data
        rabbit_messages['steps'] = steps
        print('\n', steps)

        # Battery
        battery_data = mi_band.get_battery_info()
        battery = {}
        battery['queue'] = 'battery'
        battery['mac_address'] = band
        battery['data'] = battery_data
        rabbit_messages['battery'] = battery
        print('\n', battery)

        # Heart Rate
        heart_data = mi_band.get_heart_rate_one_time()
        heart = {}
        heart['queue'] = 'heart'
        heart['mac_address'] = band
        heart['data'] = heart_data
        rabbit_messages['heart'] = heart
        print('\n', heart)

        mi_band.disconnect()

        # Send message to RabbitMQ (MQTT)
        rabbit.connection_rabbitmq()
        for queue, msg in rabbit_messages.items():
            rabbit.queue_declare(queue)
            rabbit.send(queue, str(msg))

        print(rabbit_messages)

        rabbit.connectionClose()

        sleep(35)