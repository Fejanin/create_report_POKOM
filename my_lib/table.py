class Row:
    def __new__(cls, name=None, *args, **kwargs):
        '''Создает объект класса только если передан аргумент - name.'''
        if name:
            return super().__new__(cls)

    
    def __init__(self, name, flag=False):
        self.name = name # Номенклатура
        self.units_of_measurement = None # Ед. изм.
        if flag:
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
        self.clients = {'медв': None, 'тк': None, 'атпр': None, 'пудп': None}
        self.comments = None


    def get_columns(self):
        return self.__dict__


    def __eq__(self, obj):
        if obj.__class__.__name__ == 'Row':
            return self.name == obj.name
        return self.name == obj


    def __str__(self):
        return self.name


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
        'orders_is_on_the_way': ['заказ в пути', 8],
        'pud': ['пуд', 1],
        'new_average_sales': ['ср нов', 1],
        'order': ['заказ', 1],
        'remains': ['кон ост', 1],
        'fact': ['факт', 1],
        'clients': ['опты', 4],
        'average_values': ['ср', 3],
        'comments': ['комментарии', 1],
        'sum': ['сум', 1],
        'weight': ['вес', 1]
    }
    def __init__(self):
        self.rows = []
        self.all_orders_is_on_the_way = {}
        self.all_clients = {'медв': None, 'тк', 'атпр', 'пудп'}
        self.all_average_values = {}




    def create_header(self):
        for i in self.COLUMNS:
            print([i] * self.COLUMNS[i][1])




if __name__ == '__main__':
    r1 = Row('TEST')
    print(r1.get_columns()) # получаем словарь аргументов и их значений
    r1.name = 'Obj'
    print(r1 == 'Obj') # сравнение на равенство объкта со строкой
    data = [r1]
    r2 = Row('TEST_2')
    data.append(r2)
    r2.name = 'Ok'
    r3 = Row('Test_3')
    r3.name = 'Obj'
    r4 = Row('TEST_4')
    r4.name = 'ABC'
    data.append(r4)
    print(*data)
    print('Obj' in data) # определение вхождения
    print(data.index('Obj'), data.index(r1)) # нахождение индекса объекта по имени и самому объекту
    print(r1 == r2) # Сравнение объектов по имени
    print(r1 == r3) # Сравнение объектов по имени
    # print(sorted(data)) # TypeError: '<' not supported between instances of 'Row' and 'Row'
    ##################################################



    t = Table()
    t.create_header()
