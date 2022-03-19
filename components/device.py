from port import Port


class Device:
    def __init__(self, name, number_of_ports):
        self.number_of_ports = number_of_ports
        self.name = name
    def connect(self, port:Port):
        raise NotImplementedError
    def send(self,data):
        raise NotImplementedError
    def receive(self,port:Port):
        raise NotImplementedError
