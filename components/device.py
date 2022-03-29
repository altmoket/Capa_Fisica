from abc import abstractmethod,ABCMeta
class Device(metaclass = ABCMeta):
    def __init__(self, name:str, number_of_ports:int, write_in_output):
        self.number_of_ports = number_of_ports
        self.name = name
        self.write_in_output = write_in_output

    @abstractmethod
    def disconnect_port(self, portName):
        pass

    @abstractmethod
    def getPort(self, portName):
        pass

    @abstractmethod
    def write(self, bit, message, portName):
        pass

    @abstractmethod
    def getPorts(self):
        pass
