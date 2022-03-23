from components.device import Device
class System(object):
    def __init__(self):
        self.devices = []
        pass
    def add_device(self,device:Device):
        self.devices.append(device)
        pass
    def disconnect_port(self):
        pass
    def connect_ports(self,port1,port2):
        pass
    def send(self,data, port):
        pass

