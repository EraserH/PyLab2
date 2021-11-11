import json

class Writer:

# а зачем нам вообще доп переменная в объекте?
    def __init__(self, path):
        self.__path = path

    def write_to_file(self, obj):
        with open(self.__path, 'w') as file:
            json.dump(obj, file)
            print("The object has been written to the file!")

