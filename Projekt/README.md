# Projekt zaliczeniowy 
## Wyznaczanie pary najdalszych punktów
#### Spis treści 
1. [Opis problemu](#opis-problemu)
2. [Uruchamianie](#uruchamianie)
### Opis problemu
Mając dany zbiór punktów na płaszczyźnie 2D należy znaleźć parę punktów najdalej od siebie oddalonych.
Pierwszym i zarazem najprostszym, ale nieoptymalnym sposobem (złożoność czasowa O($n^2$)) jest policzenie odległości miedzy wszystkimi parami punktów.

Lepszym (złożoność czasowa O($nlogn$)) jest wyznaczenie na początku otoczki wypukłej (convex hull) a następnie użycie metody rotating calipers.

Otoczka wypukła to nic innego jak najmniejszy wielokat, który zawiera wszytkie punkty. Poniżej znajduje się przykadowy convex hull.

![Obraz otoczki wypukłej](Pictures/convex_hull.png)

Wykonanie 

### Uruchamianie
   
