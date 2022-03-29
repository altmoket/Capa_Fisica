from time import sleep
from components.port import Port
from components.device import Device
class Hub(Device):
    def __init__(self, name:str, number_of_ports:int,write_in_output):
        Device.__init__(self,name,number_of_ports,write_in_output)
        self.port = []
        self.initialize_ports()

    def initialize_ports(self):
        for i in range(self.number_of_ports):
            port = Port(self.name+"_"+str(i+1),self)
            self.port.append(port)
            pass

    def disconnect_port(self, portName):
        for port in self.port:
            if portName.__eq__(port.name):
                port.cable.disconnect() 

    def getPorts(self):
        return self.port

    def getPort(self, portName):
        for port in self.port:
            if portName.__eq__(port.name):
                return port

    def write_in_all_ports(self, bit, portOriginName):
        for port in self.port:
            if not portOriginName.__eq__(port.name):
                port.setbit(bit)
            else:
                port.stop_transmition()
        pass

    def write(self, bit, message, portName):
        outMessage = portName + " " + "receive" + " " + str(bit) + "\n"
        self.write_in_output(self.name, outMessage)
        self.write_in_all_ports(bit, portName)

