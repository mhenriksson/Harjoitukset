lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def lista_filtteri(lista):
    parilliset = []
    for i in lista:
        if i % 2 == 0:
            parilliset.append(i)
    return parilliset

test = lista_filtteri(lista)
print(lista)
print(test)