# Projekt zaliczeniowy 
# Wyznaczanie pary najdalszych punktów
## Spis treści 
1. [Opis problemu](#opis-problemu)
2. [Zawartość plików](#zawartość-plików)
3. [Uruchamianie](#uruchamianie)
4. [Pomocna literatura](#pomocna-literatura)
### Opis problemu
Mając dany zbiór punktów na płaszczyźnie 2D należy znaleźć parę punktów najdalej od siebie oddalonych.
Pierwszym i zarazem najprostszym, ale nieoptymalnym sposobem (złożoność czasowa O($n^2$)) jest policzenie odległości miedzy wszystkimi parami punktów.

Lepszym (złożoność czasowa O($nlogn$)) sposobem jest wyznaczenie na początku otoczki wypukłej (convex hull) a następnie użycie metody rotating calipers.

Otoczka wypukła to nic innego jak najmniejszy wielokąt wypukły, który zawiera wszytkie punkty. Poniżej znajduje się przykładowy convex hull.

<img src="Pictures/convex_hull.png" alt="Alt Text" width="400" height="400">


Do wyznaczenia otoczki wypukłej mozna zastosować wiele algorytmów takich jak np. Gift wrapping, Quickhull czy Monotone chain.
###  Graham scan 
W moim przypadku użyłem algorytmu Graham scan w którym:
1. Na początku znajduję punkt `min_point` o najmniejszej wartości współrzędnej y. W przypadku, gdy istnieje więcej niż jeden punkt o tej samej wartości y,
wybierany jest punkt o najmniejszej współrzędnej x. (złożoność czasowa tej operacji to O($n$)).
2. Następnie zaczynam sortować te punkty względem punktu `min_point`(sotruję punkty ze wzgledu na kąt (rosnąco) jaki tworzą razem z `min_point` oraz osia x) używając do tego iloczynu wektorowego oraz sortowania poprzez kopcowanie (złożoność czasowa tej operacji to O($nlogn$)).
4. Potem zaczyam wyznaczać punkty, które utworza naszą otoczkę. Wykorzystuję do tego ponownie iloczyn wektorowy, który pomaga określic "orietnację punktów" -> czy punkty są ułożone zgodnie z ruchem wskazówek zagara czy też nie. (złożoność czasowa tej operacji to O($n$)). U mnie obieganie wielokąta odbywa się w przeciwnym ruchu do wskazówek zegara.

### Rotating calipers
Gdy uzyskam już punkty, które utworzą nam otoczke wypukłą, następnie używam algorytmu rotating calipers, w którym:
1. Znajuduję punkt `max_point` o największej wartości współrzędnej y. W przypadku, gdy istnieje więcej niż jeden punkt o tej samej wartości y, wybierany jest punkt o największej współrzędnej x.(złożoność czasowa tej operacji to O($n$)).
2. Następnie sprawdzam kąty, które utworzą nasze 'zaciski', i jednocześnie obliczam dystans między punktami przeciwległymi, które mogą stanowić potencjalną parę najdalszych punktów (złożoność czasowa tej operacji to O($n$)). Obrót odbywa się w kierunku przeciwnym do ruchu wskazówek zegara. <br/>
UWAGA! rysunek poniżej jest poglądowy i u mnie obrót lini równoległych jest wykonwyany w lewą stronę a nie tak jak tam w prawo.
![Obraz rotating calipers](Pictures/calipers.gif)

### Zawartość plików
`main.py` - testy na przykałdowych punktach. <br/>
`read_file.py`  -  funkcja służąca do odczytwania punktów z pliku txt. <br/>
`comapre.py` - funkcja porównująca kąt jaki tworzą punkty z osią x <br/>
`points.py` - klasa reprezentująca punkt <br/>
`heap.py` - funkcje budujące kopiec i sortujące (heapsort) <br/>
`convex_hull.py` - funkcja wyznaczająca punkty, które tworzą otoczkę wypukłą <br/>
`rotating_calipers.py` - funkcja wyznaczająca punkty przeciwlegle i obliczajaca ich dystans. Zwraca listę zawierającą największy dystans oraz punkty, które go tworzą. <br/>
`Data` - folder w którym znajdują się przykładowe punkty zapisane w plikach .txt <br/>
#### Przykładowe zbiory punktów które są testowane:
`points_1.txt`:<br/>
<br/>
<img src="Pictures/points_1.png" alt="Alt Text" width="400" height="400">
 <br/>
 <br/>
`points_2.txt`:<br/>
<br/>
<img src="Pictures/points_2.png" alt="Alt Text" width="400" height="400">
 <br/>
 <br/>
`points_3.txt`:<br/>
<br/>
<img src="Pictures/points_3.png" alt="Alt Text" width="400" height="400">
<br/>
<br/>
`points_4.txt`:<br/>
<br/>
<img src="Pictures/points_4.png" alt="Alt Text" width="400" height="400">
 <br/>
 <br/>
`points_5.txt`:<br/>
<br/>
<img src="Pictures/points_5.png" alt="Alt Text" width="400" height="400">
 <br/>
 <br/>
`points_6.txt`:<br/>
<br/>
<img src="Pictures/points_6.png" alt="Alt Text" width="400" height="400">
<br/>
<br/>
`points_7.txt`:<br/>
<br/>
<img src="Pictures/points_7.png" alt="Alt Text" width="400" height="400">
 <br/>
 <br/>
`points_8.txt`:<br/>
<br/>
<img src="Pictures/points_8.png" alt="Alt Text" width="400" height="400">

### Uruchamianie
Wystarczy uruchomić `main.py` (skorzystałem z moduły pytest do testowania).
Jeżeli chcemy przetestować działanie algorytmu na własnych punktach należy przygotowawć zwykły plik .txt (lub uzyć jednego z 5, które znajdują się w folderze Data i podmienić zawartość) i zapisać punkty w formacie `a b` gdzie `a` to wartość x punktu, a `b` to wartość y punktu. Liczby oddzielone są znakiem "spacji" czyli np. <br/>
5 5 <br/>
-3 2 <br/>
Co oznacza że mamy dwa punkty (5, 5) oraz (-3, 2).

### Pomocna literatura
https://www.cs.kent.edu/~dragan/CG/CG-Book.pdf - Opis (dłuższy) algorytmu Graham scan, szukanie srednicy convex hull (czyli szukanie pary najdalszych punktów) oraz wiele więcej informacjii odnośnie geometrii obliczeniowej. <br/>
https://en.wikipedia.org/wiki/Rotating_calipers - Opis (krótszy) odnośnie alogrytmu rotating calipers. <br/>
https://en.wikipedia.org/wiki/Graham_scan - Opis (krótszy) algorytmu Graham scan. <br/>
https://delibra.bg.polsl.pl/Content/64514/BCPS-73378_1994_Algorytm-wyznaczania.pdf - Proces (po polsku) wyznaczania otoczki wypukłej i pary najdalszych punktów.
