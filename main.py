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
print(it_validates.non_valid_data)