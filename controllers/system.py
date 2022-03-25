from components.cable import Cable
from components.device import Device
from components.computer import Computer
from components.hub import Hub
import threading
from time import sleep,time
class System(object):
    def __init__(self, signal_time = 10):
        self.devices = []
        self.time = 0
        self.isWorking = True
        self.signal_time = signal_time
        timer = threading.Thread(target=self.begin_timer,args=())
        timer.start()
        pass

    def begin_timer(self):
        while self.isWorking:
            newTime = int(round(time.time()*1000))
            if self.time < newTime:
                self.time = newTime

    def stop(self):
        self.isWorking = False

    def add_device(self,device:Device, time):
        sleep(time/1000)#1000-> 1seg = 1000milseg
        self.devices.append(device)
        outFile = open("output/"+device.name+".txt","w")
        outFile.close()

    def disconnect_port(self, portName, time):
        sleep(time/1000)
        deviceName = portName.split("_")[0]
        for device in self.devices:
            if deviceName.__eq__(device.name):
                device.disconnect_port(portName)

    def connect_ports(self,port1Name:str,port2Name,time):
        sleep(time/1000)
        port1 = None
        port2 = None
        device1Name = port1Name.split("_")[0]
        device2Name = port2Name.split("_")[0]
        for device in self.devices:
            if device1Name.__eq__(device.name):
                port1 = device.getPort(port1Name)
            elif device2Name.__eq__(device.name):
                port2 = device.getPort(port1Name)
        Cable(port1,port2)

    def send(self,data, portName,time):
        sleep(time/1000)
        deviceName = portName.split("_")[0]
        for device in self.devices:
            if deviceName.__eq__(device.name):
                device.send(data,portName)

    def execute(self,instruction):
        instruction = instruction.rstrip('\n').split(" ")
        time = int(instruction[0])
        action = instruction[1]

        if action.__eq__("create") :
            deviceType = instruction[2]
            deviceName = instruction[3]
            if deviceType.__eq__("host"):
                device = Computer(deviceName)
                pass
            else:
                numberOfPorts = int(instruction[4])
                device = Hub(deviceName,numberOfPorts)
                pass
            creator = threading.Thread(target=self.add_device,args=(device,time))
            creator.start()
            pass

        elif action.__eq__("connect"):
            port1Name = instruction[2]
            port2Name = instruction[3]
            connector = threading.Thread(target=self.connect_ports, args=(port1Name, port2Name, time))
            connector.start()
            pass

        elif action.__eq__("send"):
            portName = instruction[2]
            data = instruction[3]
            sender = threading.Thread(target=self.send,args=(data,portName,time))
            sender.start()
            pass

        elif action.__eq__("disconnect"):
            portName = instruction[2]
            disconnector = threading.Thread(target=self.disconnect_port,args=(portName, time))
            disconnector.start()
            pass

