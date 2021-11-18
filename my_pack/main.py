from .Validator import Validator
from .Writer import Writer
from .Reader import Reader
import argparse

parser = argparse.ArgumentParser("Input & output parser")
parser.add_argument(
    "-input",
    type=str,
    default="../40.txt",
    help="Input path")
parser.add_argument(
    "-output",
    type=str,
    default="../valid.txt",
    help="Output path")
pars = parser.parse_args()

path = pars.input
valid_data_path = pars.output
# invalid_data_path = 'invalid.txt'

it_reads = Reader(path)
it_writes_valid = Writer(valid_data_path)
# it_writes_invalid = Writer(invalid_data_path)
it_reads_valid = Reader(valid_data_path) # чтение валидных записей из файла

lst = it_reads.load_from_file()

it_validates = Validator(lst)

it_validates.validate()

print("Ошибки по каждому из полей: ", it_validates.non_valid_dictionary)
print()
# print(it_validates.non_valid_data)

it_writes_valid.write_to_file(it_validates.valid_data)
# it_writes_invalid.write_to_file(it_validates.non_valid_data)

# it_reads_invalid = Reader(invalid_data_path)
# print(it_reads_invalid.load_from_file())

#print(it_validates.invalid_address)


def how_much_dictionaries():
    lst = it_reads_valid.load_from_file()
    i = 0
    for dct in lst:
        i += 1
    print()
    print(f"Здесь {i} словарей")


how_much_dictionaries()