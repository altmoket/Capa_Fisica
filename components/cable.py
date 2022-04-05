
class Cable:
    def __init__(self, port1, port2):
        self.port1 = port1
        self.port2 = port2
        port1.connect(self)
        port2.connect(self)

    def read(self):
        if self.port1.transmiting and self.port2.transmiting:
            return int(self.port1.bit) ^ int(self.port2.bit)
        elif self.port1.transmiting:
            return int(self.port1.bit)
        elif self.port2.transmiting:
            return int(self.port2.bit)
        return -1

    def next_port(self, portName):
        if portName.__eq__(self.port1.name):
            return self.port2
        else:
            return self.port1 

    def transmit(self, bit, portOrigin):
        port = self.next_port(portOrigin)
        port.transmit_to_device(bit)

    def disconnect(self):
        self.port1.disconnect_cable()
        self.port2.disconnect_cable()
