#JEZYK PYTHON
#GRUPA CWICZENIOWA 02
#Zadania z zajec z dnia 23.10.2024
#Autor: Szymon Szeliga

#Funkcja pomocnicza
def is_natural_number(string) -> bool:
    try:
        number = int(string)
    except:
        return False
    else:
        if number < 0:
            return False
    return True


#ZADANIA I ICH FUNKCJE

#Zadanie 3.3
#OPIS ZADANIA
#Wypisać w pętli liczby od 0 do 30
# z wyjątkiem liczb podzielnych przez 3.
def zadanie3_3() -> None:
    print("Liczby od 0 do 30 z wyjatkiem podzielnych przez 3")
    for i in range(31):
        if i % 3 != 0:
            print(f" {i}", end='')
    print()


#Zadanie 3.4
#OPIS ZADANIA
#Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą
# x (typ float) i wypisujący x oraz trzecią potęgę x.
# Zatrzymanie programu następuje po wpisaniu z klawiatury stop.
# Jeżeli użytkownik wpisze napis zamiast liczby, to program ma
# wypisać komunikat o błędzie i kontynuować pracę.
def zadanie3_4() -> None:
    while True:
        string = input("Podaj liczbe: ")
        if string == "stop":
            break
        try:
            number = float(string)
        except:
            print("Blad, podales napis zamaist liczby, sprobuj ponownie")
        else:
            print(f"Podana liczba: {number} jej sześcian: {number * number * number} ")


#Zadanie 3.5
#OPIS ZADANIA
#Napisać program rysujący "miarkę" o zadanej długości.
# Należy prawidłowo obsłużyć liczby składające się z kilku cyfr
# (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej)
#Należy zbudować pełny string, a potem go wypisać

#Funkcja glowna
def zadanie3_5() -> None:
    string = input("Podaj dlugosc: ")
    if not is_natural_number(string):
        print("Nieprawidlowe dane")
        return
    length = int(string)

    scale = "|...."
    first_part = ''
    for i in range(length):
        first_part += scale
    first_part += '|\n'

    second_part = ''
    for i in range(length + 1):
        number = str(i)
        second_part += number + (" " * (5 - (len(str(i + 1)))))

    ruler = first_part + second_part
    print(ruler)


#Zadanie 3.6
#OPIS ZADANIA
#Napisać program rysujący prostokąt zbudowany z małych kratek.
#Należy zbudować pełny string, a potem go wypisać.
#Przykładowy prostokąt składający się 2x4 pól ma postać:
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+
def zadanie3_6() -> None:
    width_str = input("Podaj szerokosc prostokata: ")
    length_str = input("Podaj dlugosc prostokata: ")
    if not is_natural_number(width_str) or not is_natural_number(length_str):
        print("Nieprawidlowe dane!")
        return
    width = int(width_str)
    length = int(length_str)

    horizontal_part = "+---"
    vertical_part = "|   "
    horizontal_edge = ''
    vertical_edge = ''
    rectangle = ''

    for i in range(length):
        horizontal_edge += horizontal_part
        vertical_edge += vertical_part
    horizontal_edge += '+'
    vertical_edge += '|'

    for i in range(width):
        rectangle += horizontal_edge + '\n'
        rectangle += vertical_edge + '\n'
    rectangle += horizontal_edge

    print(rectangle)


#Zadanie 3.8
#OPIS ZADANIA
#Dla dwóch sekwencji liczb lub znaków znaleźć:
# (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń)
# (b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).
first_sequence = "abcdef1234xyz"
second_sequence = ['a', 'b', 'c', 'd', 'e',
                   'f', 'g', 'h', 'i', 'j', 'k', '3',
                   '4', '5', '6', 'k', 'l', 'm']

def zadanie3_8() -> None:
    first_set = set(first_sequence)
    second_set = set(second_sequence)
    intersection_result = first_set.intersection(second_set)
    sum_result =first_set.union(second_set)
    print(f"Wynik dla punktu a): {intersection_result}")
    print(f"Wynik dla punktu b): {sum_result}")


#Zadanie 3.9
#OPIS ZADANIA
#Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby.
#Znaleźć listę zawierającą sumy liczb z tych sekwencji.
#Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)], spodziewany wynik [0,4,3,7,18].
przykladowa_lista = [[], (2,2), [5,5], (), (5,5,6), [1,1,1,1,1,1]]

def zadanie3_9() -> None:
    lista_sum = []
    for i in przykladowa_lista:
         lista_sum.append(sum(i))
    print(f"Wynik: {lista_sum}")


#Zadanie 3.10
#OPIS ZADANIA
#Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim
# (z literami I, V, X, L, C, D, M) na liczby arabskie
# (podać kilka sposobów tworzenia takiego słownika).
#Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].

#Slownik mozna stworzyc w taki sposob:
#   slownik = {
#     'I': 1,
#     'V': 5,
#     'X': 10,
#     'L': 50,
#     'C': 100,
#     'D': 500,
#     'M': 1000
# }
#
#Inny sposob:
#   slownik = {}
#   slownik["I"] = 1
#   slownik["V"] = 5
#   slownik["X"] = 10
#   slownik["L"] = 50
#   slownik["C"] = 100
#   slownik["D"] = 500
#   slownik["M"] = 1000
#
#Jeszcze inaczej:
#   slownik = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

def zadanie3_10(liczba_rzymska) -> None:
    slownik = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    for i in range(len(liczba_rzymska)):
        if i > 0 and slownik[liczba_rzymska[i]] > slownik[liczba_rzymska[i - 1]]:
            result += slownik[liczba_rzymska[i]] - 2 * slownik[liczba_rzymska[i - 1]]
        else:
            result += slownik[liczba_rzymska[i]]
    print(f"Liczba {liczba_rzymska}  to: {result}")


def main() -> None:
    # zadanie3_3()
    # zadanie3_4()
    # zadanie3_5()
    # zadanie3_6()
    # zadanie3_8()
    # zadanie3_9()
    zadanie3_10("XCV")
    pass


if __name__ == "__main__":
    main()
