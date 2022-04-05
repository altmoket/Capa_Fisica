from time import sleep
from controllers.network import Network

def main():
    network=Network()
    instructions = open("script.txt",'r')
    for instruction in instructions:
        network.execute(instruction)
    sleep(2)
    network.isWorking = False
    instructions.close()

main()
