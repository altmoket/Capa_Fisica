from components.port import Port
from components.device import Device
class Computer(Device):
    def __init__(self, name:str):
        Device.__init__(self,name,1)
        self.port = Port(name+"_1",self)
        pass

    def disconnect_port(self, portName):
        return super().disconnect_port(portName)
    
    def getPort(self, portName):
        return super().getPort(portName)

    def send(self, data, portName):
        return super().send(data, portName)
