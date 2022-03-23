from components.port import Port
from components.device import Device
class Hub(Device):
    def __init__(self,name:str, number_of_ports:int):
        Device.__init__(self,name,number_of_ports)
        self.ports = []
        self.initialize_ports()
    def initialize_ports(self):
        for i in range(self.number_of_ports):
            port = Port(self.name+"_"+str(i+1),self)
            self.ports.append(port)
            pass
    def connect(self):
        raise NotImplementedError
    def send(self,data):
        raise NotImplementedError
    def read(self,port:Port):
        raise NotImplementedError
