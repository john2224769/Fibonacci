# Ejercicio N.6. repeticiones: la serie fibonacci es una serie numerica en la cual cada elemento es la suma de los dos anteriores tomando como variables los dos numeros iniciales 
# a=0 y b=1, hacer el programa en python y diagrama de flujo que calcule e imprima a partir del tercero todos los elementos de la aserie fibonacci que sean menores de 1000

from os import system

print("\n-------------------------------------------------------------")
print("-------- Elementos de la serie fibonacci menores a 1000--------")
print("-------------------------------------------------------------\n")

#processing
a=0
b=1
fib=a+b
a=a+1
b=b+1
while fib<1000:
    fib=a+b
    a=b
    b=fib
    print("\n "+str(a))

print(" ")
