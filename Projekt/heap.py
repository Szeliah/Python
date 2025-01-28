from compare import compare

# Funkcja przywracająca własność kopca
def heapify(points, n, i, min_y):
    root = i
    left = 2 * i + 1
    right = 2 * i + 2

    while True:
        if left < n and compare(min_y, points[left], points[root]) > 0:
            root = left

        if right < n and compare(min_y, points[right], points[root]) > 0:
            root = right

        if root != i:
            points[i], points[root] = points[root], points[i]
            i = root
            left = 2 * i + 1
            right = 2 * i + 2
        else:
            break

# Funkcja buduje kopiec
def build_heap(points, min_y):
    n = len(points)
    for i in range((n // 2) - 1, -1, -1):
        heapify(points, n, i, min_y)

# Funkcja sortujaca
def heap_sort(points, min_y):
    length = len(points)
    last_element_index = length - 1
    build_heap(points, min_y)

    for _ in range(length):
        points[0], points[last_element_index] = points[last_element_index], points[0]
        heapify(points, last_element_index, 0, min_y)
        last_element_index = last_element_index - 1