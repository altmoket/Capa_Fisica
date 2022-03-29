from os import close
from time import sleep
from components.port import Port
from components.device import Device
class Computer(Device):
    def __init__(self, name, time, write_in_output):
        self.time = time
        Device.__init__(self,name,1,write_in_output)
        self.port = Port(name+"_1",self)
        pass

    def disconnect_port(self, portName):
        self.port.cable.disconnect()

    def getPort(self, portName):
        return self.port

    def send(self, bits, signal_time):
        for bit in bits:
            self.port.setbit(int(bit))
            sleep(signal_time/1000)
        self.port.stop_transmition()

    def write(self, bit, message, portName):
        outMessage = portName + " " + "send" + " " + str(bit) + " " + message + "\n"
        self.write_in_output(self.name, outMessage)

    def getPorts(self):
        return self.port
