import os

##funcion que reciba cualquier cantidad de numeros (6 ,4  ) y retorne el promedio 
def promedio(*numeros):
    return sum(numeros) / len(numeros) if len(numeros) > 0 else 0

print(promedio(5 ,9))


##funcion que reciba los datos de un formulario nombre edad y carrera y que los valores los emprima en terminal 

def imprimir_formulario(nombre, edad, carrera):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Carrera: {carrera}")

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
carrera = input("Ingrese su carrera: ")
imprimir_formulario(nombre, edad, carrera)