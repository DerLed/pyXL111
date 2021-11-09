import sqlite3
import re
from openpyxl import load_workbook
import dictionary_template


def thickness_cut(thickness):
    return thickness[10:-10]


def melting_number_cut(melting_number):
    if melting_number is not None:
        return melting_number.split()[0]
    else:
        melting_number = 'Error Cell None'
        return melting_number


def batch_number_cut(batch_number):
    if batch_number is not None:
        if len(batch_number.split()) > 1:
            # return batch_number.split()[1]
            return re.sub(r"[(,)]", "", batch_number.split()[1])
        else:
            return ' '
    else:
        batch_number = 'Error Cell None'
        return batch_number


START_ROW = 5

my_workbook = load_workbook('C:/Копия журнал верификации лист 09Г2С - копия.xlsx')
my_worksheet = my_workbook.active

end_row = 5

while my_worksheet.cell(end_row, 4).value:
    end_row += 1
print(end_row)

my_db = []

for i in range(START_ROW, end_row):
    row = {}
    for key in dictionary_template.dictionary_template.keys():
        row[key] = my_worksheet.cell(i, dictionary_template.dictionary_template[key]).value
    my_db.append(row)

for it in my_db:
    print(batch_number_cut(it['batch_number']))

print()
