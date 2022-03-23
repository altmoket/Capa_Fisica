from controllers.system import System
import threading
system = System()

instructions = open("script.txt",'r')

for instruction in instructions:
    instruction = instruction.split(" ")
    action = instruction[1]
    if action.__eq__("create") :
        print("Create action")
        pass
    elif action.__eq__("connect"):
        print("Connect action")
        pass
    elif action.__eq__("send"):
        print("Send action")
        pass
    elif action.__eq__("disconnect"):
        print("Disconnect action")
        pass
    pass
instructions.close()
