import openpyxl


def get_base_form(file):
    wb = openpyxl.load_workbook(file)
    ws = wb.active

    max_col = ws.max_column
    max_row = ws.max_row

    NOMENKLATURA = ['Номенклатура', None]
    EDINICI_IZMERENIJ = ['Ед. изм.', None]
    NACHALNIJ_JSTATOK = ['Начальный остаток', None]
    PRIHOD = ['Приход', None]
    KONECHNIJ_OSTATOK = ['Конечный остаток', None]
    ALL_COLUMNS = [NOMENKLATURA, EDINICI_IZMERENIJ, NACHALNIJ_JSTATOK, PRIHOD, KONECHNIJ_OSTATOK]


    res = {}
    all_col = []

    is_once = True
    flag = False
    for row in range(1, max_row + 1):
        for col in range(1, max_col + 1):
            if not NOMENKLATURA[1]:
                if ws.cell(row = row, column = col).value == NOMENKLATURA[0]:
                    NOMENKLATURA[1] = col
            if not EDINICI_IZMERENIJ[1]:
                if ws.cell(row = row, column = col).value == EDINICI_IZMERENIJ[0]:
                    EDINICI_IZMERENIJ[1] = col
            if not NACHALNIJ_JSTATOK[1]:
                if ws.cell(row = row, column = col).value == NACHALNIJ_JSTATOK[0]:
                    NACHALNIJ_JSTATOK[1] = col
            if not PRIHOD[1]:
                if ws.cell(row = row, column = col).value == PRIHOD[0]:
                    PRIHOD[1] = col
            if not KONECHNIJ_OSTATOK[1]:
                if ws.cell(row = row, column = col).value == KONECHNIJ_OSTATOK[0]:
                    KONECHNIJ_OSTATOK[1] = col
            if NOMENKLATURA[1] and EDINICI_IZMERENIJ[1] and NACHALNIJ_JSTATOK[1] and PRIHOD[1] and KONECHNIJ_OSTATOK[1] and is_once:
                # print(NOMENKLATURA[1], EDINICI_IZMERENIJ[1], NACHALNIJ_JSTATOK[1], PRIHOD[1], KONECHNIJ_OSTATOK[1])
                all_num_col = [NOMENKLATURA[1], EDINICI_IZMERENIJ[1], NACHALNIJ_JSTATOK[1], PRIHOD[1], KONECHNIJ_OSTATOK[1]]
                is_once = False
            if ws.cell(row = row, column = col).value == 'Основной склад ПОКОМ':
                flag = True
            elif ws.cell(row = row, column = col).value == 'Склад корректировок':
                flag = False
            if flag and col in all_num_col:
                name_col = list(filter(lambda x: x[1] == col, ALL_COLUMNS))[0][0]
                value_col = ws.cell(row = row, column = col).value
                #print(f'{name_col}: {value_col}', end=' # ')
                
                if name_col == NOMENKLATURA[0]:
                    res[value_col] = {}
                    new_key = value_col
                else:
                    res[new_key].update({name_col: value_col})
    return res, ALL_COLUMNS
