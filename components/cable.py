
class Cable:
    def __init__(self, port1, port2):
        port1.connect(self)
        port2.connect(self)
        self.port1 = port1
        self.port2 = port2
    def read(self):
        if self.port1.transmiting and self.port2.transmiting:
            return self.port1.bit ^ self.port2.bit
        elif self.port1.transmiting:
            return self.port2.bit
        elif self.port2.transmiting:
            return self.port2.bit
        return None
