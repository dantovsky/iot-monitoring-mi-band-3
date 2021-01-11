from scanner import getMiBand
from auth_copy import MiBand3

# ler as mi bands
# print('\nA Band existente é: ' + getMiBand())
bands = getMiBand()

# loop das pulseiras
# para cada pulseiras no array, ler as características exidigas
for band in bands:
    print('BAND :: ' + band)
    mi_band = MiBand3(band, debug=True)
    mi_band.setSecurityLevel(level='medium') # medium
    mi_band.authenticate()

    # Steps
    steps = mi_band.get_steps()
    print('\nSteps :: ', steps)

    battery = mi_band.get_battery_info()
    print('\nBattery :: status: {}, level: {}  '.format(battery['status'], battery['level']))

    heart = mi_band.get_heart_rate_one_time()
    print('\nHeart :: ', heart)

    mi_band.disconnect()



    # band = MiBand3(MAC_ADDR, debug=True) # Get :: steps, battery, heart
    # band.setSecurityLevel(level = "medium")

    # Instanciar obj Band
    # fazer os gets

    # Enviar para o MQTT

# Coloca mi_band.disconnect()  depois de ler