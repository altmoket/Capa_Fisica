from components.port import Port
from abc import abstractmethod,ABCMeta
class Device(metaclass = ABCMeta):
    def __init__(self, name:str, number_of_ports:int):
        self.number_of_ports = number_of_ports
        self.name = name
    
    @abstractmethod
    def disconnect_port(self, portName):
        pass

    @abstractmethod
    def getPort(self, portName):
        pass

    @abstractmethod
    def send(self, data, portName):
        pass
