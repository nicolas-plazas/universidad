def palindromo(palabra):
    # Retirar lo espacios en blanco
    palabra = palabra.replace(' ', '')
    # Lower Case
    palabra = palabra.lower()
    # Invertir la palabra
    palabra_invertida = palabra[::-1]
    # Validar si el string es el mismo antes y despues de invertir retornando un booleano
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    # Recibe y almacena un valor ingresado por consola
    palabra = input('Escribe una palabra: ')
    # Llama la función "palindromo" y le pasa como parametro la palabra ingresada por consola, el resultado el almacenado en la variable
    es_palindromo = palindromo(palabra)
    # Si la variable que contiene el resultado de la función es true retorna "Es palindromo", sino lo contrario
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    run()
