# Projekt zaliczeniowy 
# Wyznaczanie pary najdalszych punktów
## Spis treści 
1. [Opis problemu](#opis-problemu)
2. [Uruchamianie](#uruchamianie)
3. [Pomocna literatura](#pomocna-literatura)
### Opis problemu
Mając dany zbiór punktów na płaszczyźnie 2D należy znaleźć parę punktów najdalej od siebie oddalonych.
Pierwszym i zarazem najprostszym, ale nieoptymalnym sposobem (złożoność czasowa O($n^2$) jest policzenie odległości miedzy wszystkimi parami punktów.

Lepszym (złożoność czasowa nlogn) jest wyznaczenie na początku otoczki wypukłej (convex hull) a następnie użycie metody rotating calipers.

Otoczka wypukła to nic innego jak najmniejszy wielokat, który zawiera wszytkie punkty. Poniżej znajduje się przykadowy convex hull.

![Obraz otoczki wypukłej](Pictures/convex_hull.png)


Do wyznaczenia otoczki wypukłej mozna zastosować wiele algorytmów takich jak np. Gift wrapping, Quickhull czy Monotone chain.

W moim przypadku użyłem algorytmu Graham scan w którym:
1. Na początku znajduję punkt `min_point` o najmniejszych współrzędnych x i y (złożoność czasowa tej operacji to O($n$)).
2. Następnie zaczynam sortować te punkty względem punktu `min_point`(sotruję punkty ze wzgledu na kąt (rosnąco) jaki tworzą razem z `min_point` oraz osia x) używając do tego iloczynu wektorowego oraz sortowania poprzez kopcowanie (złożoność czasowa tej operacji to O($nlogn$)).
3. Potem zaczyam wyznaczać punkty, które utworza naszą otoczkę. Wykorzystuję do tego ponownie iloczyn wektorowy, który pomaga określic "orietnację punktów" czy punkty są ułożone zgodnie z ruchem wskazówek zagara czy też nie i na tej podstawie odrzucam punkty, które powinny zostać pominięte. (złożoność czasowa tej operacji to O($n$)).

Gdy uzyskam już punkty, które utworzą nam otoczke wypukłą, następnie używam algorytmu rotatin calipers, który 
![Obraz rotating calipers](Pictures/calipers.gif)

### Uruchamianie
   

### Pomocna literatura
https://www.cs.kent.edu/~dragan/CG/CG-Book.pdf - Opis (dłuższy) algorytmu Graham scan, szukanie srednicy convex hull (czyli szukanie pary najdalszych punktów) oraz wiele wiecej informacji odnośnie geometrii obliczeniowej.
https://en.wikipedia.org/wiki/Rotating_calipers - Opis (krótszy) odnośnie alogrytmu rotating calipers.
https://en.wikipedia.org/wiki/Graham_scan - Opis (krótszy) algorytmu Graham scan.
