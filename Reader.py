import json

class Reader:

# а зачем нам вообще доп переменная в объекте?
    def __init__(self, path):
        self.__path = path

    def write_to_file(self, obj):
        #lst = []
        with open(self.path, 'w') as file:
            lst = json.load(file)
            print("The object has loaded from the file!")
        return lst
