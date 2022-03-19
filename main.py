from system import System

file = open("script.txt",'r')
lines = file.readlines()

print(lines)
file.close()
