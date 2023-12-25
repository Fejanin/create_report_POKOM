import openpyxl
from my_lib.table import Table, Row

def read_xlsx_file(file):

    wb = openpyxl.load_workbook(file, data_only=True)
    ws = wb.active
    max_col = ws.max_column
    max_row = ws.max_row
    return wb, ws, max_col, max_row

def create_base_table_from_dv_file(file):
    table = Table()
    wb, ws, max_col, max_row = read_xlsx_file(file)

    all_columns = {
        'name_sku': None,  # Номенклатура
        'units_of_measurement': None,  # Ед. изм.
        'initial_balance': None,  # Начальный остаток
        'receipt_of_products': None,  # Приход
        'final_balance': None  # Конечный остаток
    }

    flag = False
    for row in range(1, max_row + 1):
        for col in range(1, max_col + 1):
            if not all(all_columns.values()):
                if ws.cell(row=row, column=col).value == 'Номенклатура':
                    all_columns['name_sku'] = col
                if ws.cell(row=row, column=col).value == 'Ед. изм.':
                    all_columns['units_of_measurement'] = col
                if ws.cell(row=row, column=col).value == 'Начальный остаток':
                    all_columns['initial_balance'] = col
                if ws.cell(row=row, column=col).value == 'Приход':
                    all_columns['receipt_of_products'] = col
                if ws.cell(row=row, column=col).value == 'Конечный остаток':
                    all_columns['final_balance'] = col
            if flag and col in all_columns.values():
                # print(ws.cell(row=row, column=col).value, end=' # ')
                if col == all_columns['name_sku']:
                    current_name_row = ws.cell(row=row, column=col).value
                    table.add_row(Row(current_name_row))
                elif col == all_columns['units_of_measurement']:
                    r = table.rows[table.rows.index(current_name_row)].units_of_measurement = ws.cell(row=row, column=col).value
                elif col == all_columns['initial_balance']:
                    r = table.rows[table.rows.index(current_name_row)].initial_balance = ws.cell(row=row, column=col).value
                elif col == all_columns['receipt_of_products']:
                    r = table.rows[table.rows.index(current_name_row)].receipt_of_products = ws.cell(row=row, column=col).value
                elif col == all_columns['final_balance']:
                    r = table.rows[table.rows.index(current_name_row)].final_balance = ws.cell(row=row, column=col).value
        if ws.cell(row=row, column=1).value == 'Основной склад ПОКОМ':
            flag = True
        if ws.cell(row=row + 1, column=1).value == 'Склад корректировок':
            flag = False
    return table


