import sys

variables = []
values = []

varamt = 0

if sys.argv[1] == None:
    print("You need an argument")

file = open(sys.argv[1], 'r')
lines = file.readlines()

for linee in lines:
    line = linee.strip()
    varint = 0
    for variable in variables:
        linesep = line.split(" ")
        if linesep[0] == "var":
            if linesep[1] == variable:
                varint = varint + 1
            else:
                while line.count(variable) > 0:
                    try:
                        line = line.replace(variable, values[varint])
                    except:
                        print("\"" + line + "\" got an error")
                        print("\"" + variable + "\" caused an error maybe")
                varint = varint + 1
        else:
            while line.count(variable) > 0:
                line = line.replace(variable, values[varint])
            varint = varint + 1
    if line.startswith("printline"):
        text = line.split("\"")
        print(text[1])
    elif line.startswith("var"):
        text2 = line.split(" ")
        variables.insert(varamt, text2[1])
        values.insert(varamt, text2[3])
        varamt = varamt + 1
