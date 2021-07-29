import math


def numeros_primos(numero):
    contador_primos = 1
    numero_evaluar = 3  # Parte con el número 3, ya que el dos es obvio
    resultado = 2

    while contador_primos < numero:
        # Obtener el factorial anterior al número a evaluar
        factor = math.factorial(numero_evaluar - 1)
        # print(f'{factor} % {numero_evaluar} == {numero_evaluar} - 1')

        # Comparar el módulo del factor con las resta del número a evaluar
        if factor % numero_evaluar == numero_evaluar - 1:
            # Incremeta en 1 el contador al encontrar un número primo
            contador_primos += 1
            resultado = f'{resultado}, {numero_evaluar}'
        # Verificar el siguiente número
        numero_evaluar += 1

    print(f'Estos fueron los primeros {numero} números primos encontrados {resultado}')


def run():
    # Recibir el valor ingresado por el usuario
    numero_limite = int(input(
        'Ingrese la cantidad de numeros primos que desea conocer: '))

    # Validar que el numero sea mayor a cero
    if numero_limite > 0:
        numeros_primos(numero_limite)
    elif numero_limite == 0:
        print('El cero no es un numero primo')
    else:
        print('Debe ingresar numeros positivos')


if __name__ == '__main__':
    run()
