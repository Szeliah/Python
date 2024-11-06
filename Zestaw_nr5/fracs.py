#JEZYK PYTHON
#GRUPA CWICZENIOWA 02
#Zadania z zajec z dnia 06.11.2024
#Autor: Szymon Szeliga

import math


#Zadanie5.2
#OPIS ZADANIA
#Stworzyć plik fracs.py i zapisać w nim funkcje do działań na ułamkach.
#Ułamek będzie reprezentowany przez listę dwóch liczb całkowitych [licznik, mianownik].
#Napisać kod testujący moduł fracs.
#Nie należy korzystać z klasy Fraction z modułu fractions.
#Można wykorzystać funkcję fractions.gcd() implementującą algorytm Euklidesa.

def add_frac(frac1, frac2) -> list:                             # frac1 + frac2
    numerator = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    denominator = frac1[1] * frac2[1]
    new_frac = [numerator, denominator]
    simplest_form(new_frac)
    return new_frac


def sub_frac(frac1, frac2) -> list:                 # frac1 - frac2
    numerator = frac1[0] * frac2[1] - frac2[0] * frac1[1]
    denominator = frac1[1] * frac2[1]
    new_frac = [numerator, denominator]
    simplest_form(new_frac)
    return new_frac


def mul_frac(frac1, frac2) -> list:                 # frac1 * frac2
    numerator = frac1[0] * frac2[0]
    denominator = frac1[1] * frac2[1]
    new_frac = [numerator, denominator]
    simplest_form(new_frac)
    return new_frac



def div_frac(frac1, frac2) -> list:      # frac1 / frac2
    numerator = frac1[0] * frac2[1]
    denominator = frac1[1] * frac2[0]
    new_frac = [numerator, denominator]
    simplest_form(new_frac)
    return new_frac


def is_positive(frac) -> bool:             # bool, czy dodatni
    return frac[0] * frac[1]> 0


def is_zero(frac) -> bool:              # bool, typu [0, x]
    return frac[0] == 0


def cmp_frac(frac1, frac2) -> int:        # -1 | 0 | +1
    simplest_form(frac1)
    simplest_form(frac2)
    new_frac_1 = frac2float(frac1)
    new_frac_2 = frac2float(frac2)

    if new_frac_1 == new_frac_2:
        return 0
    elif new_frac_1 > new_frac_2:
        return 1
    else:
        return -1

def frac2float(frac) -> float:          # konwersja do float
    return float(frac[0] / frac[1])

def simplest_form(frac) -> None:                # ulamek nieskracalny
    gcd = math.gcd(frac[0], frac[1])
    frac[0] = frac[0] / gcd
    frac[1] = frac[1] / gcd



