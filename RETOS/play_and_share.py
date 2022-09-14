def getAges(number):
    for x in range(1, number + 1, +1):
        print(x)


#age = int(input("¿Cual es tu edad?"))

#getAges(age)


def getImpairs(number):
    print(1)
    for x in range(2, number + 1, +1):
        if x % 2 != 0:
            print(x)


#nro = int(input("¿Cual es tu nro?: "))
#getImpairs(nro)


def getFactorial(number):
    amount = 1
    for x in range(1, number + 1, +1):
        amount = x * amount
    print(amount)


nro2 = int(input("Dime el factorial: "))
getFactorial(nro2)
