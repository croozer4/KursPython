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