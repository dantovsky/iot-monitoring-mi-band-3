from bluepy.btle import Scanner, DefaultDelegate

# https://ianharvey.github.io/bluepy-doc/scanner.html

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
    
    
    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Discovered device", dev.addr)
        elif isNewData:
            print("Received new data from", dev.addr)
            

def getMiBand():
    print ('\nScannig for Mi Bands 3 devices...n')
    scanner = Scanner().withDelegate(ScanDelegate())
    devices = scanner.scan(5.0)

    mibandsAround = []
    for dev in devices:
        # print("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
        for (adtype, desc, value) in dev.getScanData():
            if value == 'Mi Band 3':
                mibandsAround.append(dev.addr)
        print("")

    if len(mibandsAround): # elif len(mibands_from_file) and len(mibandsAround) and mibands_from_file[0] == mibandsAround[0]:
        print('{} Mi Band 3 discovered!'.format(len(mibandsAround)))
    else:
        print('No Mi Band 3 not detected... Try again!')
    
    return mibandsAround
