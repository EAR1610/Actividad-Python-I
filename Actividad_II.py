#Eddy Alexander Reynoso Ruano Ingenieria en sistemas Ciclo I 1690-20-4610

try:
    #Se define una funcion para convertir numeros binarios a numeros decimales
    def binarioAdecimal(binario):  
         
        binario1 = binario  
        decimal, i, n = 0, 0, 0
        while(binario != 0):  
            dec = binario % 10
            decimal = decimal + dec * pow(2, i)  
            binario = binario//10
            i += 1
        return (decimal)     
  
    #Se inicializa los datos binarios 
    mensajeCodificado = input("Introduce el código en Binario: ")
   
    #Se inicializa una cadena vacia, para almacenar los datos en la cadena 
    datos =' '
   
    #La entrada se convierte a decimal y luego se convierte a cadena
    for i in range(0, len(mensajeCodificado), 8): 
      
        #colocando la variable binariosDatos del rango en el indice[0,8] 
        # y almacenarlo como entero en binariosDatos 
        binariosDatos = int(mensajeCodificado[i:i + 8]) 
       
        #Se pasa la variable binariosDatos en la funcion binarioAdecimal para obtener el valor decimal
        #de los datos de la variable binariosDatos
        datosDecimal = binarioAdecimal(binariosDatos) 
       
        #Se descifra el valor decimal devuelto por la función binarioAdecimal usando chr
        #funcion que devuelve la cadena correspondiente
        #Caracter para el valor Ascii dado y guardado en la variable datos
        datos = datos + chr(datosDecimal)  
   
    #Se imprime el resultado 
    print("El valor binario despues de la conversión es:", datos)
except ValueError:
    print("Lo siento no has dado números binarios correctos, verifícalos!")