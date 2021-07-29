def es_polidivisible(i, numero, longitud_numero):
    numero_recortado = numero[i:longitud_numero]
    numero_organizado = int(numero_recortado[::-1])
    longitud = len(numero_recortado)
    operacion = numero_organizado % longitud

    print(f'{numero_organizado} = {longitud} x {numero_organizado / longitud}')
    # print(f'modulo {operacion}')
    return operacion == 0


def numero_repetidos(numero):
    # Objeto que almacena todos los dígitos del número ingresado
    contador = {}
    # Recorrero el número, para verificar que dígitos se repiten
    for verificar in numero:
        # Verificar si el número exíste en el objeto contador
        if verificar in contador:
            # Si exíste incrementa 1 a la llave del número
            contador[verificar] += 1
        else:
            # Todos los digítos que son detectados empiezan con 1
            contador[verificar] = 1

    # Mensaje números repetidos
    for llave in contador:
        if contador[llave] > 1:
            print(
                f'los dígitos que se repiten del número ingresado son: {llave}, con la siguiente cantidad: {contador[llave]}')
        else:
            print(f'El dígito {llave} no se repite')

def run():
    numero = input('Ingrese que desea verificar: ')
    # Quitar espacios en blanco, comas o puntos
    numero = numero.replace(' ', '')
    numero = numero.replace('.', '')
    numero = numero.replace(',', '')
    longitud_numero = len(numero)

    print('<-----Números repetidos----->')
    numero_repetidos(numero)
    print('<-----Polidivisibles----->')
    numero_al_reves = numero[::-1]

    for i, digito in enumerate(numero_al_reves):
        polivisible = es_polidivisible(i, numero_al_reves, longitud_numero)

        if not polivisible:
            print('El número no es polivisible')
            break
        elif polivisible and i + 1 == longitud_numero:
            print('El número es polivisible')

if __name__ == '__main__':
    run()
