import json

class Writer:
    '''
      Объект класса Writer репрезентует запись в файл с помощью модуля json.

      Он нужен для того, чтобы записывать списки данных или словари в файлы
      при помощи модуля json

      Attributes
      ----------
        None
      '''
    def __init__(self, path):
        self.__path = path

    def write_to_file(self, obj):
        with open(self.__path, 'w') as file:
            json.dump(obj, file)
            print("The object has been written to the file!")

