from my_lib.base_func import create_base_table_from_dv_file
from my_lib.base_func import add_data_from_old_file
from my_lib.base_func import add_data_from_sales_file
from my_lib.base_func import read_xlsx_file
from my_lib.table import Row
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
pattern_current_data = r'([0-9]{2},){2}'
current_data = re.search(pattern_current_data, file_dv)[0]
print(f'{current_data = }')
table = create_base_table_from_dv_file(file_dv)


# извлекаем данные из файла прошлой недели и добавляем данные в таблицу
file_dv_old = 'дв 22,11,23пок.xlsx'
add_data_from_old_file(file_dv_old, table)


file_sales = 'пр 23-29,11,23.xlsx'
add_data_from_sales_file(file_sales, table, ('количество', 'sales'))


file_declared = 'заяв 23-29,11,23.xlsx'
add_data_from_sales_file(file_declared, table, ('Отгружено', 'declared'))
######################################################################
# dev




# вывести содержимое строк
for i in table.rows:
    print(i.get_columns())
