# from components.computer import Computer
# from controllers.system import System
# system = System()

# instructions = open("script.txt",'r')

# for instruction in instructions:
    # system.execute(instruction)
# instructions.close()


import threading
from time import sleep


class Thing:
    def __init__(self) -> None:
        self.transmition = True
        executer = threading.Thread(target=self.execute, args=())
        executer.start()
    def execute(self):
        i = 0
        while self.transmition:
            i += 1
            print("Transmition " + str(i))
        print("Transmition good")

    def stop_transmition(self):
        self.transmition = False
        print("Stopping transmition")
        

thing = Thing()
sleep(10/1000)
thing.stop_transmition()
sleep(15/1000)
