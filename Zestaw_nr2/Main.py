#JEZYK PYTHON
#GRUPA CWICZENIOWA 02
#Zadania z zajec z dnia 16.10.2024
#Autor: Szymon Szeliga



#ZMIENNE UZYWANE DO POSZCZEGOLNYCH ZADAN

#Zmienna uzyta do zadan: 2.10, 2.13, 2.14
#Przykladowy napis wielowierszowy (69 wyrazow) (369 znakow)
line = """ Lorem ipsum dolor sit amet consectetur adipiscing elit
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua
Ut enim ad minim veniam quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat
nulla pariatur Excepteur sint occaecat cupidatat non proident
sunt in culpa qui officia deserunt mollit anim id est laborum
"""

#Zmienna uzyta do zadania 2.11
#Przykladowe slowo
word = "deserunt"

#Zmienna uzyta do zadania 2.12
#Przykladowe zdanie
line_2 = "Slonce ladnie oswietla nas"

#Zmienna uzyta do zadania 2.15
#Przykladowa lista
L = [4, 1, 14, 555, 123, 9, 321]

#Zmienna uzyta do zadania 2.16
#Przykladowy napis
line_3 = """ Lorem ipsum dolor GvR amet elitsed do eiusmod tempor
GvR incididunt et GvR doloreUt enim ad minim GvR veniam
exercitation GvR ullamco laboris GvR
"""

#Zmienna uzyta do zadania 2.17
#Przykladowe zdanie
line_4 = "Za oknem świeci słońce, a liście drzew delikatnie tańczą na wietrze"

#Zmienna uzyta do zadania 2.18 (30 zer)
#Przykladowa liczba
number = 312302130123021032678100087680123120321031230120306756701230213012301030012300120302000000

#Zmienna uzyta do zadania 2.19
#Przykladowa lista z liczbami
L_2 = [0, 321, 54, 1, 67, 187, 104, 9, 12, 56, 3, 60]



#ZADANIA I ICH FUNKCJE

#Zadanie 2.10
#OPIS ZADANIA
#Mamy dany napis wielowierszowy line.
#Podac sposob obliczenia liczby wyrazow w napisie.
#Przez wyraz rozumiemy ciag "czarnych" znakow, oddzielony
# od innych wyrazow bialymi znakami (spacja, tabulacja, newline).
def zadanie2_10(text) -> None:
    words = text.split()
    print(f"Liczba wyrazow w napisie line = {len(words)}\n")


#Zadanie 2.11
#OPIS ZADANIA
#Podać sposób wyświetlania napisu word tak,
# aby jego znaki były rozdzielone znakiem podkreślenia
def zadanie2_11(string) -> None:
    characters = list(string)
    result = '_'.join(characters)
    print(f"Napis word po rozdzieleniu go znakiem (_) = {result}\n")


#Zadanie 2.12
#OPIS ZADANIA
#Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line.
#Zbudować napis stworzony z ostatnich znaków wyrazów z wiersza line.
def zadanie2_12(text) -> None:
    words = text.split()
    lista_1 = []
    lista_2 = []
    for i in words:
        lista_1.append(i[0])
        lista_2.append(i[-1])
    wr_1 = ''.join(lista_1)
    wr_2 = ''.join(lista_2)
    print(f"Nowe slowo zbudowane z pierwszych liter wyrazow z napisu line_2 = {wr_1}\n")
    print(f"Nowe slowo zbudowane z ostatnich liter wyrazow z napisu line_2 = {wr_2}\n")


#Zadanie 2.13
#OPIS ZADANIA
#Znaleźć łączną długość wyrazów w napisie line.
#Wskazówka: można skorzystać z funkcji sum().
def zadanie2_13(text) -> None:
    words = text.split()
    lista = []
    for i in words:
        lista.append(len(i))
    print(f"Laczna dlugosc wyrazow w napisie line = {sum(lista)}\n")


#Zadanie 2.14
#OPIS ZADANIA
#Znaleźć: (a) najdłuższy wyraz,
#(b) długość najdłuższego wyrazu w napisie line.
def zadanie2_14(text) -> None:
    words = text.split()
    lista = []
    for i in words:
        lista.append(len(i))
    length = max(lista)
    longest_word = words[lista.index(length)]
    print(f"Najdluzszy wyraz = {longest_word}, dlugosc tego wyrazu = {length}\n")


#Zadanie 2.15
#OPIS ZADANIA
#Na liście L znajdują się liczby całkowite dodatnie.
#Stworzyć napis będący ciągiem cyfr kolejnych liczb z listy L.
def zadanie2_15(L) -> None:
    lista = []
    for i in L:
        lista.append(str(i))
    string = ''.join(lista)
    print(f"Napis skladajacy sie z cyfr z listy L = {string}\n")


#Zadanie 2.16
#OPIS ZADANIA
#W tekście znajdującym się w zmiennej line
#zamienić ciąg znaków "GvR" na "Guido van Rossum".
def zadanie2_16(text) -> None:
    new_line = text.replace("GvR", "Guido van Rossum")
    print(f"Tekst po zastapieniu GvR na Guido van Rossum = {new_line}\n")


#Zadanie 2.17
#OPIS ZADANIA
#Posortować wyrazy z napisu line raz alfabetycznie,
# a raz pod względem długości.
#Wskazówka: funkcja wbudowana sorted()
def zadanie2_17(text) -> None:
    words = text.split()
    words_length = sorted(words, key=len)
    words_alpha = sorted(words, key=str.casefold)
    print(f"Posortowane wyrazy alfabetycznie = {words_alpha}\n")
    print(f"Posortowane wyrazy pod wzgledem dlugosci = {words_length}\n")


#Zadanie 2.18
#OPIS ZADANIA
#Znaleźć liczbę cyfr zero w dużej liczbie całkowitej.
#Wskazówka: zamienić liczbę na napis
def zadanie2_18(big_number) -> None:
    string = str(big_number)
    zeros_counter = string.count('0')
    print(f"Licza cyfr zero = {zeros_counter}\n")


#Zadanie 2.19
#OPIS ZADANIA
#Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie.
# Chcemy zbudować napis z trzycyfrowych bloków,
# gdzie liczby jedno- i dwucyfrowe będą miały blok dopełniony zerami,
# np. 007, 024. Wskazówka: str.zfill()
def zadanie2_19(numbers) -> None:
    lista = []
    for i in numbers:
        temp = str(i)
        lista.append(temp.zfill(3))
    text = " ".join(lista)
    print(f"Napis z trzycyfrowych blokow = {text}\n")



def main() -> None:
    #zadanie2_10(line)
    #zadanie2_11(word)
    #zadanie2_12(line_2)
    #zadanie2_13(line)
    #zadanie2_14(line)
    #zadanie2_15(L)
    #zadanie2_16(line_3)
    #zadanie2_17(line_4)
    #zadanie2_18(number)
    #zadanie2_19(L_2)
    pass

if __name__ == "__main__":
    main()

