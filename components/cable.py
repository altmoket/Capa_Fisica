
class Cable:
    def __init__(self, port1, port2):
        self.port1 = port1
        self.port2 = port2
        port1.connect(self)
        port2.connect(self)

    # def read(self):
        # if self.port1 and self.port2 and self.port1.transmiting and self.port2.transmiting:
            # return self.port1.bit ^ self.port2.bit
        # elif self.port1 and self.port1.transmiting:
            # return self.port2.bit
        # elif self.port2 and self.port2.transmiting:
            # return self.port2.bit
        # return None

    def next_port(self, portName):
        if portName.__eq__(self.port1.name):
            return self.port2
        else:
            return self.port1 

    def disconnect(self):
        self.port1.disconnect_port()
        self.port2.disconnect_port()
