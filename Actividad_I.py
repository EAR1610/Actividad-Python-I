#Alumno: Eddy Alexander Reynoso Ruano. Ingeniería en sistemas Ciclo I. Carné: 1690-20-4610

lista = [] #se declara una lista para almacenar los datos introducidos por el usuario
control=1 #Se declara una variable encargada de llevar el control, ya que son 5 números que se le pide al usuario
while control<6: #Se hace uso del bucle while para pedir los números y almacenarlos en una lista
    try:
        numero=int(input(f"Dame el numero {control}: "))
        lista.append(numero)
        control=control+1
    except ValueError:
        print("Debes de introducir solo números")

#Se crea una variable de tipo entero que almacenará el número en el que el usuario desea que se le muestren los númeors, seguidamente esta variable se comparara mediante un if
opcion=int(input("¿Como deseas que se muestren los números? \n 1 = forma ascendente 2 = forma descendente (1 o 2): "))
pares=[] #Se crea una lista llamada Pares para almacenar todos los números pares en la lista en donde el usuario almacena los números
impares=[] #Se crea una lista llamada imPares para almacenar todos los números impares en la lista en donde el usuario almacena los números
#Se utiliza el condicional IF para evaluar condiciones
if opcion==1: 
    print("Lista ordenada (ascendente) : {0}".format(sorted(lista)))

    for n in lista: #se utiliza un for para recorrer la lista y posteriormente mediante un if conocer si el número es par o impar
        if (n % 2 == 0):
            pares.append(n)
        if (n % 2 != 0):
            impares.append(n)
    if not pares: #Se declara un if para verificar si las lista pares esta vacia en caso contrario hay numeros pares
        print("No hay números pares")
    else:
        print("Los números pares son:")
        for i in pares:
            print(i)
    if not impares: #Se declara un if para verificar si las lista impares esta vacia en caso contrario hay numeros impares
        print("No hay números impares")
    else:
        print("Los números impares son:")
        for i in impares:
            print(i)
#Se utiliza el Elif 
elif opcion==2:
    print("Lista ordenada (descendente): {0}".format(sorted(lista,reverse=True)))
    for n in lista:
        if (n % 2 ==0):
            pares.append(n)
        if (n % 2 !=0):
            impares.append(n)
    if not pares: #Se declara un if para verificar si las lista pares esta vacia en caso contrario hay numeros pares
        print("No hay números pares")
    else:
        print("Los números pares son:")
        for i in pares:
            print(i)
    if not impares: #Se declara un if para verificar si las lista impares esta vacia en caso contrario hay numeros impares
        print("No hay números impares")
    else:
        print("Los números impares son:")
        for i in impares:
            print(i)
#Uso del Else
else:
    print("No me has dado un número determinado \n debes elegir 1 o 0")
