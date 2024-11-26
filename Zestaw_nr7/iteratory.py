#JEZYK PYTHON
#GRUPA CWICZENIOWA 02
#Zadania z zajec z dnia 20.11.2024
#Autor: Szymon Szeliga

import random
import itertools

# Zadanie 7.6
# OPIS ZADANIA
#Stworzyć następujące iteratory nieskończone:
#(a) zwracający 0, 1, 0, 1, 0, 1, ...,
#(b) zwracający przypadkowo jedną wartość z ("N", "E", "S", "W") [błądzenie przypadkowe na sieci kwadratowej 2D],
#(c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia].


#Podpunkt a)
def iterator_a():
    iterator = itertools.cycle("01")
    for i in range(10):
        print(next(iterator), end=", ")
    print()


#Podpunkt b)
def iterator_b():
    cardinal_direction = ('N', 'E', 'S', 'W')
    iterator = (random.choice(cardinal_direction) for i in range(8))
    for j in iterator:
        print(j, end=", ")
    print()


#Podpunkt c)
def iterator_c():
    iterator = itertools.cycle(range(7))
    for i in range(14):
        print(next(iterator), end=", ")
    print()


def main():
    iterator_a()
    iterator_b()
    iterator_c()


if __name__ == "__main__":
    main()