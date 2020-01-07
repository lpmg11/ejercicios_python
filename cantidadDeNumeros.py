if __name__ == "__main__":
    cero = 0
    mayores = 0
    menores = 0
    c=int(input("Ingrese la cantidad de numeros: "))
    for i in range (c):
        n = int(input("Ingrese un numero: "))
        if n > 0:
            mayores = mayores + 1
        elif n < 0:
            menores = menores + 1
        else:
            cero = cero + 1
    print("Los numeros mayores a 0 son: ", mayores)
    print("Los numeros menores a 0 son: ", menores)
    print("Los numeros iguales 0 son: ", cero)
