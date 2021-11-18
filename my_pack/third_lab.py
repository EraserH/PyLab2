from my_pack.Reader import Reader
from my_pack.Writer import Writer
import re

read_path = "../valid.txt"
sorted_path = "../3lab.json"


class Sorter:
    @staticmethod
    def __heapify(arr, n, i, dct_index): # массив, размер кучи, индекс корня, поле, по которому сортируем
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i][dct_index] < arr[l][dct_index]:
            largest = l

        if r < n and arr[largest][dct_index] < arr[r][dct_index]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            Sorter.__heapify(arr, n, largest, dct_index)

    @staticmethod
    def heap_sort(arr, dct_index):
        n = len(arr)

        # Построение max-heap.
        for z in range(n, -1, -1):
            Sorter.__heapify(arr, n, z, dct_index)

        # Один за другим извлекаем элементы
        for z in range(n - 1, 0, -1):
            arr[z], arr[0] = arr[0], arr[z]
            Sorter.__heapify(arr, z, 0, dct_index)


def write_sorted_to_file(index='height'):
    read_valid = Reader(read_path)
    lst = read_valid.load_from_file()

    for dct in lst:
        dct['height'] = float(dct['height'])
        dct['inn'] = int(dct['inn'])
        dct['passport_series'] = int(re.sub(r'\s', '', dct['passport_series']))
        dct['passport_series'] = int(dct['passport_series'])
        dct['work_experience'] = int(dct['work_experience'])

    '''for i in range(3):
        # print(lst[i].values())
        for j in lst[i].values():
            if not isinstance(j, str):
                print(type(j), end='\t')
                print(j)
        print()'''

    fields = [keys for keys, values in lst[0].items() if not isinstance(values, str)]
    print("Поля:")
    print('     '.join(fields))

    # choice = int(input("По какому полю отсортировать?"))

    Sorter.heap_sort(lst, index)

    write_sorted = Writer(sorted_path)
    write_sorted.write_to_file(lst)

    read_valid = Reader(sorted_path)
    lst_2 = read_valid.load_from_file()

    print()
    for i in range(50000):
        print(lst_2[i])


#write_sorted_to_file('height')

'''print()
for i in range(10000):
    print(lst[i])'''

