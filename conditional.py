number: int = input("Coloca el número: ")
#if (int(number) >= 0):
#    print("El número es positivo")
#else:
#    print("El número es negativo")

result = pow(int(number), 2)

if (int(result) >= 0):
    print(f"El número {number} es positivo because {result}")
else:
    print(f"El número {number} es negativo because {result}")
