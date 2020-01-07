suma = 0
c = 0

def numeros(suma, c):
    n = int(input("Ingrese un numero: "))
    if n !=0:
        suma = suma + n
        c = c + 1
        numeros(suma,c)
    else:
        print("La suma de los numeros ingresados es: ", suma)
        print("La media de los numeros es: ", suma/c)


if __name__ == "__main__":
    numeros(suma , c)

