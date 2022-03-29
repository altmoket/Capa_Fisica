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
        # reader = threading.Thread(target = self.read_from_cable, args=())
        # reader.start()
        pass

    def read_from_cable(self):
        while self.cableConnected():
            bitReceived = self.cable.read()
            if bitReceived != -1:
                self.device.write(bitReceived, "ok", self.name)

    def setbit(self,bit):
        if self.cableConnected():
            self.bit = bit
            self.transmiting = True
            bitReceived = self.cable.read()
            while bitReceived!=-1 and bitReceived != bit and self.cableConnected():
                self.device.write(bit, "collision", self.name)
                self.transmiting = False
                sleep(5/1000)
                self.transmiting = True
                bitReceived = self.cable.read()
            self.device.write(bit, "ok", self.name)


    def stop_transmition(self):
        self.transmiting = False

    def disconnect_cable(self):
        self.stop_transmition()
        del(self.cable)
        pass

    def cableConnected(self)->bool:
        if hasattr(self, "cable"):
            return True
        return False
