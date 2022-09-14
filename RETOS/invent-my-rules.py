def ejercicio1():
  a = int(input("Ingrese el primer numero: "))
  b = int(input("Ingrese el segundo numero: "))
  print((a+b)/2)

def ejercicio2():
  a = int(input("Ingrese el primer numero: "))
  b = int(input("Ingrese el segundo numero: "))
  print(a**b)

def ejercicio3():
  a = int(input("Ingrese el numero: "))
  print(a**(1/2))

def ejercicio4():
  a = int(input("Ingrese el primer numero: "))
  b = int(input("Ingrese el segundo numero: "))
  print((a**2+ b**2)**(1/2))


print("Ingrese numero de ejercicio: ")
num = int(input())
if num == 1:
  ejercicio1()
elif num == 2:
  ejercicio2()
elif num == 3:
  ejercicio3()
elif num == 4:
  ejercicio4()