import random as r

numero = r.randint(0,100)
i = 0

def adivina(i, numero):
    print ("Tienes ",10-i," intentos")
    n=int(input("Ingresa un numero: "))
    if n<numero:
        print("El numero ingresado es menor")
        if i<9:
            i=i+1
            adivina(i,numero)
        else:
            print("Fallaste ")
            print("El numero es: ", numero)
    elif n > numero:
        print("El numero ingresado es mayor ")
        if i < 9:
            i = i+1
            adivina(i, numero)
        else:
            print("Fallaste ")
            print("El numero es: ", numero)
    else:
        print("Lo lograste adivinaste el numero")

if __name__ == '__main__':
    print (numero)
    adivina(i,numero)
