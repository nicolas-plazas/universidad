def par_o_impar(numero):
    modulo = numero % 2

    if modulo != 0:
        return {
            'es_par': 'impar',
            'tipo_operacion': 'multiplicacion',
            'resultado_operacion': numero * numero
        }
    else:
        return {
            'es_par': 'par',
            'tipo_operacion': 'suma',
            'resultado_operacion': numero + numero
        }


def run():
    numero = input('Digite un numero: ')
    es_par, tipo_operacion, resultado_operacion = par_o_impar(int(numero)).values()

    print(f'El numero ingresado es {es_par} y resultado de la {tipo_operacion} es {resultado_operacion}')


if __name__ == '__main__':
    run()
