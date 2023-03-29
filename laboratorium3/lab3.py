# przechwytywanie wyjątków

# pierwszy sposób

# def odwroc_wartosc(tablica: list, indeks: int) -> float:
#     if indeks >= len(tablica):
#         raise IndexError("Indeks poza zakresem")
#     if tablica[indeks] == 0:
#         raise ZeroDivisionError("Nie można dzielić przez zero")
#     return 1/tablica[indeks]

# print(odwroc_wartosc([3, 4, 7, 0], 3))

# drugi sposób

# def odwroc_wartosc2(tablica: list, indeks: int) -> float:
#     try:
#         return 1/tablica[indeks]
#     except IndexError:
#         print("Indeks poza zakresem")
#     except ZeroDivisionError:
#         print("Nie można dzielić przez zero")

# print(odwroc_wartosc2([3, 4, 7, 0], 3))

# trzeci sposób 

# def odwroc_wartosc3(tablica: list, indeks: int) -> float:
#     try:
#         return 1/tablica[indeks]
#     except (IndexError, ZeroDivisionError):
#         print("Błąd indeksu lub dzielenia przez zero")

# print(odwroc_wartosc3([3, 4, 7, 5], 1))

# zadanie domowe 1 

def odwroc_wartosc3(tablica: list, indeks: int) -> float:
    try:
        return 1/tablica[indeks]
    except (IndexError, ZeroDivisionError):
        print("Błąd indeksu lub dzielenia przez zero")
    finally:
        print("Koniec")

print(odwroc_wartosc3([3, 4, 7, 5], 1))

# zadanie domowe 2
# return blokował działanie klauzuli else

def odwroc_wartosc3(tablica: list, indeks: int) -> float:
    try:
        result = 1/tablica[indeks]
    except (IndexError, ZeroDivisionError):
        print("Błąd indeksu lub dzielenia przez zero")
    else:
        print("Tutaj wykonały się instrukcje z klauzuli else")
        print("Wynik: ", result)
    finally:
        print("Koniec")

print(odwroc_wartosc3([3, 4, 7, 5], 1))
