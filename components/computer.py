from components.port import Port
from components.device import Device
class Computer(Device):
    def __init__(self, name:str):
        Device.__init__(self,name,1)
        self.port = Port(name+"_1",self)
        pass
    def connect(self):
        pass

