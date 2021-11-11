import json
import re
from Validator import Validator
from Writer import Writer
from Reader import Reader

path = "40.txt"

it_reads = Reader(path)
it_writes = Writer(path)

lst = it_reads.load_from_file(path)
print(type(lst[0]))

it_validates = Validator(lst)

it_validates.validate()

print(it_validates.non_valid_dictionary)
print()
# print(it_validates.non_valid_data)
'''z = 0
for i in it_validates.invalid_university:
    if z > 1000:
        break
    print(i)
    z += 1'''

print(it_validates.invalid_address)

#main_pattern = r'([Уу]ниверситет|[Аа]кадеми[яи]|[Пп]олитехнический|[И|и]нститут|им.|[А-Я]{3,}|РФ|СП[Бб]ГУ|[Пп]олитех|[Ии]сследовательский)'
# print(re.search(main_pattern, 'МФТИ'))