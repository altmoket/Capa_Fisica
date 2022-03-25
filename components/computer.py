from components.port import Port
from components.device import Device
class Computer(Device):
    def __init__(self, name:str):
        Device.__init__(self,name,1)
        self.port = Port(name+"_1",self)
        pass

    def disconnect_port(self, portName):
        self.port.cable.disconnect()

    def getPort(self, portName):
        return self.port

    def send(self, data, portName):
        return super().send(data, portName)
