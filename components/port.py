import threading
from time import sleep
class Port:
    def __init__(self, name, device):
        self.name = name
        self.device = device
        self.transmiting = False
        self.reading = False

    def connect(self, cable):
        self.cable = cable
        pass

    def transmit_to_device(self, bit):
        if bit != -1:
            self.device.write(bit,"receive",self.name)
        else:
            self.device.write(bit,"stop_transmition", self.name)

    def transmit(self, bit):
        if self.cableConnected():
            self.bit = bit
            self.transmiting = True
            self.cable.transmit(bit, self.name)


    def setbit(self, bit):
        if self.cableConnected():
            self.bit = bit
            self.transmiting = True
            bitReceived = self.cable.read()
            while self.cableConnected() and bitReceived != bit:
                self.device.write(bit, "collision", self.name)
                self.transmiting = False
                sleep(5/1000)
                self.transmiting = True
                if self.cableConnected():
                    bitReceived = self.cable.read()
            self.device.write(bit, "send", self.name)
            self.cable.transmit(bit, self.name)


    def stop_transmition(self):
        self.transmiting = False
        if self.cableConnected():
            self.cable.transmit(-1, self.name)

    def disconnect_cable(self):
        self.stop_transmition()
        del(self.cable)
        pass

    def cableConnected(self)->bool:
        if hasattr(self, "cable"):
            return True
        return False
