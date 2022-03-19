from components.device import Device
class System(object):
    def __init__(self):
        self.devices = []
        pass
    def addDevice(self,device:Device):
        self.devices.append(device)
        pass
