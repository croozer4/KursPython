import os

sciezka = input("Podaj sciezke do pliku: ");

if os.path.isfile(sciezka):
    print("Sciezka do pliku jest prawidlowa");
else:
    print("Sciezka do pliku jest nieprawidlowa");
    exit();

rozszerzenie = os.path.splitext(sciezka)[1];
print("Plik ma rozszerzenie " + rozszerzenie); 