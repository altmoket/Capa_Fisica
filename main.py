from controllers.system import System
system = System()

instructions = open("script.txt",'r')

for instruction in instructions:
    system.execute(instruction)
instructions.close()
