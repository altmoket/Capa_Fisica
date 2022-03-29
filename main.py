from time import sleep
from controllers.system import System
system = System()

instructions = open("script.txt",'r')

for instruction in instructions:
    system.execute(instruction)
instructions.close()

def print_devices_info(devices):
    for device in devices:
        print("Device: " + device.name)
        if device.number_of_ports == 1:
            port = device.getPorts() 
            print(device.name + " -> " + port.name)
            if port.cableConnected():
                print(port.name + " ::connected with:: " + port.cable.next_port(port.name).name)
        elif device.number_of_ports > 1:
            ports = device.getPorts()
            for port in ports:
                print(device.name + " -> " + port.name)
                if port.cableConnected():
                    print(port.name + " ::connected with:: " + port.cable.next_port(port.name).name)
                pass
        pass
sleep(2)
devices = system.getDevices()
print_devices_info(devices)
system.isWorking = False
