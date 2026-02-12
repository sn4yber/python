def saludo():
    print("Hola, bienvenido a Python")


def saludar(nombre):
    print(f"Hola {nombre}, ¡bienvenido!")


def sumar(a, b):
    return a + b


def es_par(numero):
    return numero % 2 == 0


def area_rectangulo(base, altura):
    return base * altura


def tabla(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


def cuadrado_y_cubo(n):
    return n ** 2, n ** 3


def agregar_numero(lista, numero):
    lista.append(numero)


if __name__ == "__main__":
    saludo()
    saludar("snayber")

    resultado = sumar(5, 3)
    print(f"La suma es: {resultado}")

    print(f"¿Es 4 par? {es_par(4)}")
    print(f"¿Es 7 par? {es_par(7)}")

    area = area_rectangulo(5, 10)
    print(f"El área del rectángulo es: {area}")

    print("\nTabla del 5:")
    tabla(5)

    cuadrado, cubo = cuadrado_y_cubo(3)
    print(f"\nCuadrado de 3: {cuadrado}")
    print(f"Cubo de 3: {cubo}")

    mi_lista = [1, 2, 3]
    agregar_numero(mi_lista, 5 ,6 ,7)
    print(f"\nLista después de agregar 4: {mi_lista}")
