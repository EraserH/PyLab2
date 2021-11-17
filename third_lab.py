from Reader import Reader
from Writer import Writer
import re

read_path = "valid.txt"
sorted_path = "3lab.json"


# Процедура для преобразования в двоичную кучу поддерева с корневым узлом i, что является индексом в arr[]. n - размер кучи
def heapify(arr, n, i, dct_index):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and arr[i][dct_index] < arr[l][dct_index]:
        largest = l

    if r < n and arr[largest][dct_index] < arr[r][dct_index]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, dct_index)


# Основная функция для сортировки массива заданного размера
def heapSort(arr, dct_index):
    n = len(arr)

    # Построение max-heap.
    for i in range(n, -1, -1):
        heapify(arr, n, i, dct_index)

    # Один за другим извлекаем элементы
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # свап
        heapify(arr, i, 0, dct_index)


# Управляющий код для тестирования
'''arr = [ 12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
    print ("%d" %arr[i]),'''

read_valid = Reader(read_path)
lst = read_valid.load_from_file()

for dct in lst:
    dct['height'] = float(dct['height'])
    dct['inn'] = int(dct['inn'])
    dct['passport_series'] = int(re.sub(r'\s', '', dct['passport_series']))
    dct['passport_series'] = int(dct['passport_series'])
    dct['work_experience'] = int(dct['work_experience'])

for i in range(3):
    # print(lst[i].values())
    for j in lst[i].values():
        if not isinstance(j, str):
            print(type(j), end='\t')
            print(j)
    print()

fields = [keys for keys, values in lst[0].items() if not isinstance(values, str)]
print("Поля:")
print('     '.join(fields))

# choice = int(input("По какому полю отсортировать?"))

heapSort(lst, 'height')

'''print()
for i in range(100000):
    print(lst[i])'''

write_sorted = Writer(sorted_path)
write_sorted.write_to_file(lst)

read_valid = Reader(sorted_path)
lst_2 = read_valid.load_from_file()

print()
for i in range(50000):
    print(lst_2[i])