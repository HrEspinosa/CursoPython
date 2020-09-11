
# Ejercicio 1
operacion = 4 < 2
print(type(operacion))


#Ejercicio 2
nombre = "Heri Espinosa"
print("Bienvenido "+ nombre)


#Ejercicio 3
numero = 15
if numero % 2 == 0:
    print("El Numero es Par")
else:
    print("El Numero es Impar")


#Ejercicio 4
print("Evaluar dos Numeros!!")
numero1 = input("Escriba el Primer numero: ")
numero2 = input("Escriba el Segundo numero: ")
print(numero1 > numero2)


#Ejercicio 5
print("El valor del Dollar es: 58")
dollar = input("Escriba la Cantidad de Dollar que desea convertir: ")
dollar = float(dollar)
tasa = 58.50
print(dollar * tasa)


#Ejercicio 6
celsius = input("Convertir Grados Celsius a Fahrenheit: ")
celsius = float(celsius)
convercion = (celsius * 1.8) + 32
print(convercion)


#Ejercicio 7
nota1 = input("Ingrese La Nota Numero 1: ")
nota2 = input("Ingrese La Nota Numero 2: ")
nota3 = input("Ingrese La Nota Numero 3: ")
nota4 = input("Ingrese La Nota Numero 4: ")
nota1 = int(nota1)
nota2 = int(nota2)
nota3 = int(nota3)
nota4 = int(nota4)

sumatoria = (nota1 + nota2 + nota3 + nota4)
totalnota = (sumatoria / 4)
if(totalnota <= 40):
    print("Su Nota es: F")
elif(totalnota <=60):
    print("Su Nota es: E")
elif(totalnota <=70):
    print("Su Nota es: D")
elif(totalnota <=80):
    print("Su Nota es: C")
elif(totalnota <=90):
    print("Su Nota es: B")
elif(totalnota <=100):
    print("Su Nota es: A")
else:
    print("Hay un Error!!, Vuelva a Ingresar las Notas Nuevamente")


#Ejercicio 8
monto = input("Saludos, Ingrese el Monto del Prestamo Solicitado: ")
monto = float(monto)
print("NOTA!! Tenemos Disponibilidad desde 1 hasta 8 años en Plazo de Pago")
plazo = input("Ingrese el Plazo a Pagar del Prestamo Solicitado: ")
plazo = int(plazo)
print("Solo para Recordar Nuestro interes Fijo en Prestamos es de 5%")
cant_cuota = (plazo * 12)
print("Catidad de Cuotas a Pagar: " + str(cant_cuota))
int(cant_cuota)
interesanual = (5/100)
interesesporano = (monto * interesanual)
interesespormes = (interesesporano / 12)
totalintereses = (interesesporano * plazo)
pagomes = (monto / cant_cuota) + interesespormes 
pagototal = monto + (interesesporano * plazo)
print("Su Cuota Mensual tendra un Valor de: " + str(pagomes) + " Pesos")
print("Su Total a Pagar en "+ str(plazo) +" Años es: "+ str(pagototal) + " Pesos")

