from scanner import getMiBand
from auth import MiBand3
import rabbitmq
import time

# Object instatiation
rabbit = rabbitmq.RabbitMQ()

# ler as mi bands
# print('\nA Band existente é: ' + getMiBand())

# Variables
bands = getMiBand()
rabbit_messages = {}

print('\n» Getting data from Mi Band 3...')

# loop das pulseiras
# para cada pulseiras no array, ler as características exidigas
def countdown(t):
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1

while True:
    for band in bands:
        print('Mi Band with MAC Address ' + band + '\n')
        mi_band = MiBand3(band, debug=True)
        mi_band.setSecurityLevel(level='medium') # medium
        mi_band.authenticate()

        # Steps
        steps = mi_band.get_steps()
        rabbit_messages['steps'] = steps
        print('\nSteps :: ', steps)

        # Battery
        battery = mi_band.get_battery_info()
        rabbit_messages['battery'] = battery
        print('Battery :: status: {}, level: {}  '.format(battery['status'], battery['level']))

        print('\n» Getting heart in real time. Please use your Mi Band 3 and wait for a while...')

        # Heart Rate
        heart = mi_band.get_heart_rate_one_time()
        rabbit_messages['heart'] = heart
        print('Heart :: ', heart)

        mi_band.disconnect()

        # Send message to RabbitMQ
        rabbit.connection_rabbitmq()
        for queue, msg in rabbit_messages.items():
            # print(queue, ' -> ', str(msg))
            # print('type of :: ', type(str(msg)))
            rabbit.queue_declare(queue)
            rabbit.send(queue, str(msg))

        rabbit.connectionClose()

        countdown(120)

        # band = MiBand3(MAC_ADDR, debug=True) # Get :: steps, battery, heart
        # band.setSecurityLevel(level = "medium")

        # Instanciar obj Band
        # fazer os gets

        # Enviar para o MQTT

'''
Exemplo da balança -> para o Mosquitto mas adaptável para o Rabbit

'''

