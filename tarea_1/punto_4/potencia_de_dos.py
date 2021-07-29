import math

def es_ptencia_de_dos(numero):
    if numero < 1:
        return False

    # Regresar al número base
    log = math.log(numero, 2)
    # Si el resultado del anterior proceso es correcto, sé regresa
    # el número base ej: 2.0, se redondea y resta, si el resultado es
    # igual a 0 retorna True de lo contrario un False
    return 0 == (log - int(log))

def run():
    numero = int(input('Ingrese el número que desea validar: '))
    print(es_ptencia_de_dos(numero))


if __name__ == '__main__':
    run()
