from points import Point

#Parsowanie danych
def parse_data(data):
    return float(data) if data else None


#Czytanie danych z pliku i dodawanie do listy
def read_file(text_file) -> list:
    list_points = []
    with open(text_file, "r") as file:
        for line in file:
            numbers = line.strip().split()
            if len(numbers) == 2:
                point = Point(parse_data(numbers[0]), parse_data(numbers[1]))
                list_points.append(point)
    return list_points