from components.port import Port
from components.device import Device
class Hub(Device):
    def __init__(self, name:str, number_of_ports:int):
        Device.__init__(self,name,number_of_ports)
        self.port = []
        self.initialize_ports()

    def initialize_ports(self):
        for i in range(self.number_of_ports):
            port = Port(self.name+"_"+str(i+1),self)
            self.port.append(port)
            pass

    def disconnect_port(self, portName):
        for port in self.port:
            if portName.__eq__(port.name):
                port.cable.disconnect() 

    def getPort(self, portName):
        for port in self.port:
            if portName.__eq__(port.name):
                return port

    def send(self, data, portName):
        return super().send(data, portName)
