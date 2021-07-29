def fibonacci(numero):
    if numero < 2:
        return numero
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)


def run():
    numero_limite = int(
        input('Digite cuantos numeros que desea ver de la sequencia de fibonacci: '))

    if numero_limite >= 0:
        for i in range(numero_limite):
            print(fibonacci(i))
    else:
        print('El numero ingresado debe ser mayor o igual a cero')


if __name__ == '__main__':
    run()
