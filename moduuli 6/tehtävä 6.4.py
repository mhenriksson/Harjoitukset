lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def listansumma(lista):
    summa = 0
    for i in lista:
        summa += i
    return summa

summa = listansumma(lista)
print(f'Summa:  {summa}')