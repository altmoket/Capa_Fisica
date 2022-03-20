from components.port import Port

class Device:
    def __init__(self, name:str, number_of_ports:int):
        self.number_of_ports = number_of_ports
        self.name = name
    def connect(self):
        raise NotImplementedError
    def send(self,data):
        raise NotImplementedError
    def read(self,port:Port):
        raise NotImplementedError
