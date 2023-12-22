from my_lib.base_func import create_base_table_from_dv_file
from my_lib.base_func import read_xlsx_file
import os
import re


# получаем список файлов для обработки
all_files_list = [i for i in os.listdir() if '.xlsx' in i]
groups_of_files = {
    'движение': [re.findall(r'дв ([0-9]+,){2}[0-9]+пок\.xlsx', i) for i in all_files_list],
    'оптовики': None,
    'продажи': None,
    'заявлено': None
}




# за основу берем файл движения
file_dv = 'дв 29,11,23пок.xlsx'
table = create_base_table_from_dv_file(file_dv)

'''
for i in table.get_rows():
    print(i.name, i.units_of_measurement, i.initial_balance, i.receipt_of_products, i.final_balance)
'''

# файл расчета прошлой недели













'''
file_sales = 'пр 23-29,11,23.xlsx'

columns = {'Номенклатура': None, 'количество': None}

workbook, worksheet, max_col, max_row = read_xlsx_file(file_sales)
for row in range(1, max_row + 1):
    if all(columns.values()):
        print()
    for col in range(1, max_col + 1):
        if worksheet.cell(row=row, column=col).value in columns: # находим колонки: Номенклатура и количество
            if not columns[worksheet.cell(row=row, column=col).value]:
                columns[worksheet.cell(row=row, column=col).value] = col # связываем название колонки с ее номером
        if col in columns.values():
            print(worksheet.cell(row=row, column=col).value, end=' # ')
'''