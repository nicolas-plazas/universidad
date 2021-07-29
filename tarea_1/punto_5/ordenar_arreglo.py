def run():
    # Listas desorganizadas
    lista_texto = ['mouse', 'teclado', 'computador', '*']
    print(f'Lista con string en desorden {lista_texto}')
    lista_texto.sort()
    print(f'Lista con string en organizada {lista_texto}')
    lista_enteros= [100, 1, 50]
    print(f'Lista con enteros en desorden {lista_enteros} y organizada {lista_enteros.sort()}')

if __name__ == '__main__':
    run()