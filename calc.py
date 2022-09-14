number_1 = input("Ingrese el primer número: ")
while number_1.isnumeric() == False:
    number_1 = input("Ingrese el 1er número correctamente: ")
number_2 = input("Ingrese el segundo número: ")
while number_2.isnumeric() == False:
    number_2 = input("Ingrese el 2er número correctamente: ")
operation = input("Ingrese la operación: ")

while operation not in ("+", "-", "*", "/"):
    operation = input("Coloque uno de los signos disponibles => +, -, *, /: ")
result = 0
number_1 = int(number_1)
number_2 = int(number_2)
if (operation == "+"):
    result = number_1 + number_2
elif operation == "-":
    result = number_1 - number_2
elif operation == "*":
    result = number_1 * number_2
else:
    if number_2 == 0:
        print("si quiere dividir... el número 2 debe ser mayor a 0 \n")
    else:
        result = number_1 / number_2
print("El resultado de la operación ", operation, " es", result)
