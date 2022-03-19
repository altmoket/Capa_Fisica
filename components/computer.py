from device import Device
from cable import Cable
class Computer(Device):
    def __init__(self, name):
        super.__init__(name,1)
        pass
    def connect(self, device:Device):
        pass
