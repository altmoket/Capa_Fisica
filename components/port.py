import threading


class Port:
    def __init__(self, name:str, device):
        self.name = name
        self.device = device
        self.transmiting = False
        self.reading = False

    def connect(self, cable):
        self.cable = cable
        listener = threading.Thread(target=self.getData,args=())
        listener.start()
        pass

    def setData(self,bit):
        if self.cableConnected():
            self.bit = bit
            self.transmiting = True
    def getData(self):
        if self.cableConnected():
            return self.cable.read()
    def stop_transmition(self):
        self.transmiting = False

    def disconnect_cable(self):
        del(self.cable)
        pass
    def cableConnected(self)->bool:
        if self.cable:
            return True
        return False
