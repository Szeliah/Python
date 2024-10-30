#JEZYK PYTHON
#GRUPA CWICZENIOWA 02
#Zadania z zajec z dnia 30.10.2024
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


#Zadanie 4.2
#OPIS ZADANIA
#Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji
# które zwracają pełny string przez return.
#Funkcje nie powinny pytać użytkownika o dane
# tylko korzystać z argumentów.
#def make_ruler(n): pass
#def make_grid(rows, cols): pass
def make_ruler(n):
    if not is_natural_number(n):
        raise ValueError("Bledne dane!")
    length = int(n)
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
    return ruler


def make_grid(rows, cols):
    if not is_natural_number(rows) or not is_natural_number(cols):
        raise ValueError("Bledne dane!")
    width = int(rows)
    length = int(cols)

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

    return rectangle


#Zadanie 4.3
#OPIS ZADANIA
#Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.
def factorial(n):
    if n < 0:
        raise ValueError("Nieprawidlowa liczba")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


#Zadanie 4.4
#OPIS ZADANIA
#Napisać iteracyjną wersję funkcji fibonacci(n)
# obliczającej n-ty wyraz ciągu Fibonacciego.
def fibonacci(n):
    if n < 0:
        raise ValueError("Nieprawidlowa liczba")
    if n == 0:
        return 0

    temp_1 = 0
    temp_2 = 1
    result = 1

    for i in range(n - 1):
        result = temp_1 + temp_2
        temp_1 = temp_2
        temp_2 = result
    return result


#Zadanie 4.5
#OPIS ZADANIA
#Napisać funkcję odwracanie(L, left, right) odwracającą
# kolejność elementów na liście od numeru left do right włącznie.
#Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.

#FUNKCJA ODWRACANIE ITERACYJNIE
def odwracanie_iter(L, left, right):
    if right > len(L) -1  or left > right or left < 0:
        raise ValueError("Nieprawidlowe dane!")
    index = right
    mean = ((left + right + 1) // 2)
    for i in range(left, mean):
        L[i], L[index] = L[index], L[i]
        index = index - 1


#FUNKCJA ODWRACANIE IREKURENCYJNIE
def odwracanie_rek(L, left, right):
    if left >= right:
        return
    if right > len(L) - 1 or left > right or left < 0:
        raise ValueError("Nieprawidlowe dane!")
    L[left], L[right] = L[right], L[left]
    return odwracanie_rek(L, left + 1, right - 1)


#Zadanie 4.6
#OPIS ZADANIA
#Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji,
# która może zawierać zagnieżdżone podsekwencje. Wskazówka: rozważyć wersję rekurencyjną,
# a sprawdzanie, czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple))
def sum_seq(sequence):
    result = 0
    for i in sequence:
        if isinstance(i, (list, tuple)):
            result = result + sum_seq(i)
        else:
            result = result + i
    return result


#Zadanie 4.7
#OPIS ZADANIA
#Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami,
# a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości.
#Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich elementów sekwencji.
#Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie czy element
# jest sekwencją, wykonać przez isinstance(item, (list, tuple)).
def flatten(sequence) -> list:
    lista = []
    for i in sequence:
        if isinstance(i,(list, tuple)):
            lista.extend(flatten(i))
        else:
            lista.append(i)
    return lista



def main() -> None:
    # print(make_ruler(5))
    # print(make_grid(3, 5))
    # print(factorial(6))
    # print(fibonacci(12))
    L_1 = [1, 2, 3, 4, 5]
    L_2 = [5, 6, 7, 8, 9]
    odwracanie_iter(L_1, 2, 4)
    odwracanie_rek(L_2, 2, 4)
    print(L_1)
    print(L_2)
    seq_1 = [1, [2], [3, 4], 5, (6, 7, [8, 9]), 10]
    seq_2 = [1, 2, [2, 3], 9, (10 , 10)]
    print(sum_seq(seq_1))
    print(flatten(seq_2))


if __name__  == "__main__":
    main()
