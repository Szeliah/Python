# Zestaw_nr3

### Zadanie_3.1

##### Czy podany kod jest poprawny składniowo w Pythonie? Jeśli nie, to dlaczego?

`x = 2; y = 3;`<br>
`if (x > y):`<br>
`    result = x;`<br>
`else:`<br>
    `result = y;`<br>
Tutaj jest wszystko ok, poza tym że średniki nie są wymagane.

` for i in "axby": if ord(i) < 100: print (i) `
Kod jest niepoprawny, brak wcięć po instrukcji for i if 

`for i in "axby": print (ord(i) if ord(i) < 100 else i)`
 Kod poprawny

---

### Zadanie_3.2


##### Co jest złego w kodzie:
`L = [3, 5, 4] ; L = L.sort()`
Funkcja sort() zwraca None , wiec w tym przypadku L będzie miało wartość None.
Dodatkowo można usunąć średnik i dodać nową linię.

`x, y = 1, 2, 3`
Za dużo wartości do przypisania, tylko dwie zmienne a trzy wartości.

`X = 1, 2, 3 ; X[1] = 4`
Nie można zmienić wartości w krotkach (niemutowalne)

`X = [1, 2, 3] ; X[3] = 4`
Brak indeksu 3, poprawne indeksy to 0,1 i 2.
Wysątpi IndexError

`X = "abc" ; X.append("d")`
Metoda append() dostępna dla listy a nie dla stringów.

`L = list(map(pow, range(8)))`
Brak argumentów w funkcji pow(), można użyć wyrażenia lambda

---

W pliku `Main.py` znajdują sie rozwiązania do zadań od 3.3 do 3.10 bez 3.7.
Każde zadanie ma swoją funkcje czyli np. zadanie 3.10 ma funkcje ` zadanie3_10() `
Aby skorzystać z danej funkcji wystarczy w głównej funkcji (`main()`) odkomentować daną funckje.   
