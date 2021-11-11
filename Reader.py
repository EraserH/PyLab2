import json

class Reader:
    '''
        Объект класса Reader репрезентует чтение из файла с помощью модуля json.

        Он нужен для того, чтобы считывать в структуры python списки данных или словари
        из файлов при помощи модуля json

        Attributes
        ----------
        None
    '''
    def __init__(self, path):
        self.__path = path

    def load_from_file(self):
        #lst = []
        with open(self.__path, 'r') as file:
            lst = json.load(file)
            print("The object has been loaded from the file!")
        return lst
