import sys

if sys.argv[1] == None:
    print("You need an argument")

file = open(sys.argv[1], 'r')
lines = file.readlines()

for line in lines:
    if line.startswith("printline"):
        text = line.split("\"")
        print(text[1])
        
