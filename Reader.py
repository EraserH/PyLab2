import json

class Reader:

# а зачем нам вообще доп переменная в объекте?
    def __init__(self, path):
        self.__path = path

    def load_from_file(self, obj):
        #lst = []
        with open(self.__path, 'r') as file:
            lst = json.load(file)
            print("The object has been loaded from the file!")
        return lst
