class Row:
    flag = False
    def __new__(cls, name=None, *args, **kwargs):
        '''Создает объект класса только если передан аргумент - name.'''
        if name:
            return super().__new__(cls)

    
    def __init__(self, name):
        self.name = name # Номенклатура
        self.units_of_measurement = None # Ед. изм.
        self.promotion = None # Акция, не для Симферополя !!!!!!!!!!!!!!!!!!!!!!
        self.initial_balance = None # Начальный остаток
        self.receipt_of_products = None # Приход
        self.sales = None # Продажи
        self.final_balance = None # Конечный остаток
        self.mark = None # Метка
        self.multiplicity = None # Кратность
        self.expiration_dates = None # Сроки годности
        self.declared = None # Заявлено
        self.diff = None # разность между заявлено и отгружено
        self.orders_is_on_the_way = {} # Заказы в пути {'29,11,': 50, '01,12,: 120}
        self.new_average_sales = None # self.sales / 5
        self.average_values = {}  # средние значения продаж => {'17,11,': 100, '24,11,': 111, ...}
        self.medvedev_sales = None # медв
        self.tk_sales = None # тк
        self.atamanov_sales = None # атпр
        self.pud_sales = None # пудп
        self.comments = None # комментарии
        self.sum = None # сум
        self.weigth = None # вес
        self.flag = True # после __init__, изменение атрибутов после прохождения проверки


    def get_columns(self):
        return self.__dict__


    def __eq__(self, obj):
        if obj.__class__.__name__ == 'Row':
            return self.name == obj.name
        return self.name == obj

    def __lt__(self, obj):
        if obj.__class__.__name__ == 'Row':
            return self.name < obj.name
        return self.name < obj


    def __str__(self):
        return self.name


    def __setattr__(self, key, value):
        if self.flag:
            # print('\nFLAG => TRUE')
            # print(f'{key = }, {value = }')
            # TODO присвоение данных в словари должно проходить проверку!!!
            pass
        self.__dict__[key] = value


class Table:
    COLUMNS = {
        'name': ['Номенклатура', 1],
        'units_of_measurement': ['Ед. изм.', 2],
        'initial_balance': ['Начальный остаток', 3],
        'receipt_of_products': ['Приход', 4],
        'sales': ['Расход', 5],
        'final_balance': ['Конечный остаток', 6],
        'mark': ['метка', 7],
        'multiplicity': ['крат', 8],
        'expiration_dates': ['сроки', 9],
        'declared': ['заяв', 10],
        'diff': ['разн', 11],
        'orders_is_on_the_way': ['заказ в пути', {12: None, 13: None, 14: None, 15: None, 16: None, 17: None, 18: None}],
        'pud_order': ['пуд', 19],
        'new_average_sales': ['ср нов', 20],
        'krim_order': ['заказ', 21],
        'remains': ['кон ост', 22],
        'fact': ['факт', 23],
        'medvedev_sales': ['медв', 24],
        'tk_sales': ['тк', 25],
        'atamanov_sales': ['атпр', 26],
        'pud_sales': ['пудп', 27],
        'average_values': ['ср', {28: None, 29: None, 30: None}],
        'comments': ['комментарии', 1],
        'sum': ['сум', 31],
        'weight': ['вес', 32]
    }
    START_HEADER = 3
    START_ROWS = 6
    ORDERS_IS_ON_THE_WAY = {}
    AVERAGE_VALUES = {}
    
    def __init__(self):
        self.rows = []
        self.date = None


    def add_row(self, row):
        self.rows.append(row)


    def create_header(self):
        print(vars(Table)['COLUMNS'])


    def get_rows(self):
        '''
        Return sorted list self.rows
        '''
        return sorted(self.rows)




if __name__ == '__main__':
    r1 = Row('TEST')
    print(f"{r1.get_columns() = }") # получаем словарь аргументов и их значений
    r1.name = 'Obj'
    print(f"{r1 == 'Obj' = }") # сравнение на равенство объкта со строкой
    data = [r1]
    r2 = Row('TEST_2')
    data.append(r2)
    r2.name = 'Ok'
    r3 = Row('Test_3')
    r3.name = 'Obj'
    r4 = Row('TEST_4')
    r4.name = 'ABC'
    data.append(r4)
    print('data =', *data)
    print(f"{'Obj' in data = }") # определение вхождения
    print(f"{data.index('Obj') = }, {data.index(r1) = }") # нахождение индекса объекта по имени и самому объекту
    print(f"{r1 == r2 = }") # Сравнение объектов по имени
    print(f"{r1 == r3 = }") # Сравнение объектов по имени
    sorted_list = sorted(data)
    print(f"{sorted_list = }")
    print(*[(i, i.name) for i in sorted_list], sep='\n')
    ##################################################

    t = Table()
    t.create_header()
    t.add_row(r1)
    t.add_row(r2)
    t.add_row(r4)
    print(f"{t.get_rows() = }")
    print(f"{t.get_rows().index('ABC') = }")
    
