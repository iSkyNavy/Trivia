def printText(veces, word):
    for x in range(0, int(veces), +1):
        print(word + "\n")


#printText(5, "jeje")

#for x in range(10, -1, -1):
#    print(x, "\n")

files = int(input("Por favor, ingrese el número de filas: "))


def printTriangle(fils):
    for x in range(1, fils + 1, +1):
        #print("*" * x)
        for y in range(0, x, +1):
            print("*", end="")
        print("\n")


printTriangle(files)
