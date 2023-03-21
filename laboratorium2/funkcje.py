# Zadanie 1
print ("Zadanie 1")

def polacz_imie_nazwisko(imie, nazwisko):
    return f"{imie} {nazwisko}"

print(polacz_imie_nazwisko("Jan", "Kowalski"))

# Zadanie 2
print ("Zadanie 2")

def wypisz_liczby_parzyste(liczba_elementow):
    for i in range(2, liczba_elementow + 1, 2):
        print(i, end=" ")

wypisz_liczby_parzyste(10)
print()

# Zadanie 3
print ("Zadanie 3")

def addDict(dict1, dict2):
    return {**dict1, **dict2}

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

dict3 = addDict(dict1, dict2)

print(dict3)

# Zadanie 4
print ("Zadanie 4")

def podnies_do_kwadratu(lista):
    return [x**2 for x in lista]

lista = [1, 2, 3, 4, 5]
listaNowa = podnies_do_kwadratu(lista)

print(listaNowa)