import re


class Validator:

    def __init__(self, lst):
        self.__data = lst

        self.__invalid_university = []
        self.__invalid_address = []

        self.__valid_data = []
        self.__non_valid_data = []
        self.__non_valid_dictionary = { # это можно сделать генератором!
            "telephone": 0,
            "height": 0,
            "inn": 0,
            "passport_series": 0,
            "university": 0,
            "work_experience": 0,
            "academic_degree": 0,
            "worldview": 0,
            "address": 0
        }

    def __convert_to_str(self, dct):
        print("метод convert: ", type(dct))
        for field in dct.values():
            field = str(field)
        print(dct)
        return dict(dct)

    def __check_telephone(self, val): # готово
        val = str(val)
        if re.fullmatch(r'\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}', val) != None:
            return True
        return False

    def __check_height(self, val):
        #if re.match(r'', dict["height"]) != None:
        val = str(val)
        if re.fullmatch(r'[0-9]+\.[0-9]+|[0-9]+', val) != None:
            if 1.3 < float(val) < 2.7:
                return True
        return False

    def __check_inn(self, val): # готово
        val = str(val)
        if re.fullmatch(r'\d{12}', val) != None:
            return True
        return False

    def __check_passport_series(self, val): # готово
        val = str(val)
        if re.fullmatch(r'\d{2} \d{2}', val) != None:
            return True
        return False

    def __check_university(self, val): #
        val = str(val)
        # if re.fullmatch(r'[-\sа-яА-Я\.]+', val) != None:
        pattern = r'([Уу]ниверситет|[Аа]кадеми[яи]|[Пп]олитехнический|[И|и]нститут|им.|[А-Я]{3,}|РФ|СП[Бб]ГУ|[Пп]олитех|[Ии]сследовательский)'
        if re.search(pattern, val) != None:
            return True
        return False

    def __check_work_experience(self, val): # готово
        val = str(val)
        if re.fullmatch(r'\d{1,2}', val) != None:
            return True
        return False

    def __check_academic_degree(self, val):
        val = str(val)
        if re.fullmatch(r'Бакалавр|Специалист|Магистр|Кандидат наук|Доктор наук', val) != None:
            return True
        return False

    def __check_worldview(self, val):
        val = str(val)
        if re.fullmatch(r'[-а-яА-Я0-9\s]+', val) != None:
            return True
        return False

    def __check_address(self, val):
        val = str(val)
        if re.fullmatch(r'[-а-яА-Я0-9)(\s\.]+\s[0-9]{1,5}', val) != None:
            return True
        return False



    def validate(self):
        for dct in self.__data:
            # print("метод validate: ", type(dct))
            # print(dct)
            # dct = self.__convert_to_str(dct)
            is_valid = True

            if not self.__check_telephone(dct["telephone"]):
                self.non_valid_dictionary["telephone"] += 1
                is_valid = False
            if not self.__check_height(dct["height"]):
                self.non_valid_dictionary["height"] += 1
                is_valid = False
            if not self.__check_inn(dct["inn"]):
                self.non_valid_dictionary["inn"] += 1
                is_valid = False
            if not self.__check_passport_series(dct["passport_series"]):
                self.non_valid_dictionary["passport_series"] += 1
                is_valid = False
            if not self.__check_university(dct["university"]):
                self.non_valid_dictionary["university"] += 1
                self.__invalid_university.append(dct["university"])
                is_valid = False
            if not self.__check_work_experience(dct["work_experience"]):
                self.non_valid_dictionary["work_experience"] += 1
                is_valid = False
            if not self.__check_academic_degree(dct["academic_degree"]):
                self.non_valid_dictionary["academic_degree"] += 1
                is_valid = False
            if not self.__check_worldview(dct["worldview"]):
                self.non_valid_dictionary["worldview"] += 1
                is_valid = False
            if not self.__check_address(dct["address"]):
                self.non_valid_dictionary["address"] += 1
                self.__invalid_address.append(dct["address"])
                is_valid = False

            if is_valid:
                self.__valid_data.append(dct)
            else:
                self.__non_valid_data.append(dct)

    @property
    def non_valid_dictionary(self):
        return self.__non_valid_dictionary

    @property
    def non_valid_data(self):
        return self.__non_valid_data

    @property
    def valid_data(self):
        return self.__valid_data

    @property
    def invalid_university(self):
        return self.__invalid_university

    @property
    def invalid_address(self):
        return self.__invalid_address



