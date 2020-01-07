def vocales():
    v = input("Ingrese un caracter: ")
    if (v == "a" or v == "e" or v == "i" or v == "o" or v == "u"):
        print("VOCAL")
        vocales()
    elif (v == " "):
        pass
    else:
        print("NO VOCAL")
        vocales()


if __name__ == "__main__":
    vocales()
