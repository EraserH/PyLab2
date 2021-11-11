import json
import re
from Validator import Validator
from Writer import Writer
from Reader import Reader

path = "40.txt"
valid_data_path = 'valid.txt'
invalid_data_path = 'invalid.txt'

it_reads = Reader(path)
it_writes_valid = Writer(valid_data_path)
it_writes_invalid = Writer(invalid_data_path)

lst = it_reads.load_from_file()
print(type(lst[0]))

it_validates = Validator(lst)

it_validates.validate()

print(it_validates.non_valid_dictionary)
print()
# print(it_validates.non_valid_data)

it_writes_valid.write_to_file(it_validates.valid_data)
it_writes_invalid.write_to_file(it_validates.non_valid_data)

it_reads_invalid = Reader(invalid_data_path)
print(it_reads_invalid.load_from_file())

#print(it_validates.invalid_address)

#main_pattern = r'([Уу]ниверситет|[Аа]кадеми[яи]|[Пп]олитехнический|[И|и]нститут|им.|[А-Я]{3,}|РФ|СП[Бб]ГУ|[Пп]олитех|[Ии]сследовательский)'
# print(re.search(main_pattern, 'МФТИ'))