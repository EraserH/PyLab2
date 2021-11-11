import re


class Validator:

    def __init__(self, lst):
        self.__data = lst

    def __check_telephone(self, dict): # готово
        if re.fullmatch(r'\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}', dict['telephone']) != None:
            return True
        return False

    def __check_height(self, dict):
        #if re.match(r'', dict["height"]) != None:
        if re.fullmatch(r'[0-9]+\.[0-9]+|[0-9]+', dict["height"]) != None:
            if 1.3 < float(dict["height"]) < 2.7:
                return True
        return False

    def __check_inn(self, dict): # готово
        if re.fullmatch(r'\d{12}', dict["inn"]) != None:
            return True
        return False

    def __check_passport_series(self, dict): # готово
        if re.fullmatch(r'\d{2} \d{2}', dict["passport_series"]) != None:
            return True
        return False

    def __check_university(self, dict): #
        if re.fullmatch(r'[-\sа-яА-Я]+', dict["university"]) != None:
            return True
        return False

    def __check_work_experience(self, dict): # готово
        if re.fullmatch(r'\d{1,2}', dict["work_experience"]) != None:
            return True
        return False

    def __check_academic_degree(self, dict):
        if re.fullmatch(r'Бакалавр|Специалист|Магистр|Кандидат наук|Доктор наук', dict["academic_degree"]) != None:
            return True
        return False

    def __check_worldview(self, dict):
        if re.fullmatch(r'[-а-яА-Я0-9\s]+', dict["worldview"]) != None:
            return True
        return False

    def __check_address(self, dict):
        if re.fullmatch(r'[-а-яА-Я0-9\s]+', dict["address"]) != None:
            return True
        return False



    def validate(self):
        for dict in self.data:
            if not self.__check_telephone(dict["telephone"]):
                continue



print('Hello!!!!!!')
obj = Validator([1, 2, 3])
if obj.check_height('Cool!') == True:
    print("Nice")
else:
    print("Baad!")

