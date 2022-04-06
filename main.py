from time import sleep
from controllers.network import Network

def main():
    instructions = open("script.txt",'r')
    configurations = open("config.txt",'r')
    signal_time=10
    exit_time=2
    for config in configurations:
        config = config.rstrip('\n').split("=")
        print(config)
        if config[0].__eq__("signal_time"):
            signal_time = int(config[1])
        elif config[0].__eq__("exit_time"):
            exit_time = float(config[1])
    network=Network(signal_time)
    for instruction in instructions:
        network.execute(instruction)
    sleep(exit_time)
    network.stop()
    instructions.close()
    configurations.close()

main()
