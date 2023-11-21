while True:
    print("MENU:")
    print("1. Suma")
    print("2. Producto entre números")
    print("3. División entre 2 números")
    print("4. Calcular factorial")
    print("5. Imprimir tablas de multiplicar")
    print("6. Calcular cuadrado y cubo")
    print("7. Calcular promedio")
    print("8. Encontrar máximo y mínimo")
    print("9. Salir")

    escoger=int(input("ingrese el numero que desea:"))

    if escoger == 1:
        cantidad = int(input("Ingrese la cantidad de números que desea sumar: "))
        suma = 0
        for uwu in range(cantidad):
            numeros = float(input(f"Ingrese el número {uwu + 1}: "))
            suma += numeros
        print("El resultado sumado es:", suma)
    elif escoger==2:
        cantidad=int(input("Escribe el primer numero que desea sumar:"))
        producto=1
        for uwu in range(cantidad):
            numeros=float(input(f"Ingresa los numeros {uwu + 1}:"))
            producto*=numeros
        print("El resultado del producto es:", producto)
    elif escoger==3:
        numero1=float(input("Ingresa el primer numero:"))
        numero2=float(input("Ingresa el segundo numero:"))
        if numero2 !=0:
            division=numero1/numero2
            print("El resultado de la division es:", division)
        else:
            print("No se puede dividir entre 0.")
    elif escoger==4:
        numero=int(input("Ingresa un numero para calcular su factorial:"))
        factorial=1
        if numero < 0:
            print("No se puede hacer con numeros negativos")
        elif numero==0:
            print("El factorial de 0 es 1")
        else:
            for uwu in range(1,numero+1):
                factorial*=uwu
            print(f"El factorial de {numero} es: {factorial}")
    elif escoger == 5:
        num = int(input("Ingresa un numero: "))
        print(f"Tabla de multiplicar de {num}:")
        for uwu  in range(1, 11):
            print(f"{num} x {uwu} = {num * uwu}")
    elif escoger == 9:
        print("Cerrando")
        break
    else:
        print("No se encuentra esa opcion")