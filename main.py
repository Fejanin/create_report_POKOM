from my_lib.base_func import create_base_table_from_dv_file
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

'''
for i in table.get_rows():
    print(i.name, i.units_of_measurement, i.initial_balance, i.receipt_of_products, i.final_balance)
'''

# файл расчета прошлой недели
file_dv_old = 'дв 22,11,23пок.xlsx'
wb, ws, max_col, max_row = read_xlsx_file(file_dv_old)

all_columns = {
    'name_sku': None, # Номенклатура
    'units_of_measurement': None, # Ед. изм.,
    'mark': None, # метка
    'multiplicity': None, # крат
    'expiration_dates': None, # сроки
    'orders_is_on_the_way': {}, # заказ в пути
    'medvedev_sales': None, # медв
    'tk_sales': None, # тк
    'atamanov_sales': None, # атпр
    'pud_sales': None, # пудп
    'average_values': {}, # ср: {'10,11,': 28, ...}
    'comments': None, # комментарии
}

columns_val = []
columns_dict = []

for row in range(1, max_row + 1):
    current_sku = None
    current_obj = None
    for col in range(1, max_col + 1):
        if not all(all_columns.values()):
            if ws.cell(row=row, column=col).value == 'Номенклатура':
                all_columns['name_sku'] = col
                columns_val.append(col)
            if ws.cell(row=row, column=col).value == 'Ед. изм.':
                all_columns['units_of_measurement'] = col
                columns_val.append(col)
            if ws.cell(row=row, column=col).value == 'метка':
                all_columns['mark'] = col
                columns_val.append(col)
            if ws.cell(row=row, column=col).value == 'крат':
                all_columns['multiplicity'] = col
                columns_val.append(col)
            if ws.cell(row=row, column=col).value == 'сроки':
                all_columns['expiration_dates'] = col
                columns_val.append(col)
            if ws.cell(row=row, column=col).value == 'заказ в пути':
                if ws.cell(row=row + 1, column=col).value:
                    all_columns['orders_is_on_the_way'].update({ws.cell(row=row + 1, column=col).value: col})
                    columns_dict.append(col)
            if ws.cell(row=row, column=col).value == 'медв':
                all_columns['medvedev_sales'] = col
                columns_val.append(col)
            if ws.cell(row=row, column=col).value == 'тк':
                all_columns['tk_sales'] = col
                columns_val.append(col)
            if ws.cell(row=row, column=col).value == 'атпр':
                all_columns['atamanov_sales'] = col
                columns_val.append(col)
            if ws.cell(row=row, column=col).value == 'пудп':
                all_columns['pud_sales'] = col
                columns_val.append(col)
            if ws.cell(row=row, column=col).value == 'ср':
                if ws.cell(row=row + 1, column=col).value:
                    all_columns['average_values'].update({ws.cell(row=row + 1, column=col).value: col})
                    columns_dict.append(col)
            if ws.cell(row=row, column=col).value == 'комментарии':
                all_columns['comments'] = col
                columns_val.append(col)
        if all(all_columns.values()) and col == all_columns['name_sku'] and ws.cell(row=row, column=col).value:
            current_sku = ws.cell(row=row, column=col).value
            if not current_sku in table.rows: # Добавить СКЮ, которого нет в новом движении
                table.add_row(Row(current_sku))
            current_obj = table.rows[table.rows.index(current_sku)]
        if all(all_columns.values()) and current_sku and col in columns_val:
            name_col = list(filter(lambda x: x[1] == col, all_columns.items()))[0][0]
            if name_col == 'name_sku':
                continue
            current_obj.__dict__[name_col] = ws.cell(row=row, column=col).value
        elif all(all_columns.values()) and current_sku and col in columns_dict:
            if col in all_columns['orders_is_on_the_way'].values():
                value = ws.cell(row=row, column=col).value
                if value == '#REF!':
                    value = 0
                current_obj.__dict__['orders_is_on_the_way']\
                    [list(filter(lambda x: x[1] == col, all_columns['orders_is_on_the_way'].items()))[0][0]] = value
            elif col in all_columns['average_values'].values():
                value = ws.cell(row=row, column=col).value
                current_obj.__dict__['average_values'] \
                    [list(filter(lambda x: x[1] == col, all_columns['average_values'].items()))[0][0]] = value
            else:
                raise Exception('NOT FOUND!!!')


for i in table.get_rows():
    print(i.get_columns())



"""
print(all_columns)
print(columns_val)
print(columns_dict)

print(all(all_columns.values()))
print(*[str(i) for i in table.get_rows()], sep='\n')
"""



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