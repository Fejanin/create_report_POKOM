class Row:
    def __new__(cls, name=None, *args, **kwargs):
        '''Создает объект класса только если передан аргумент - name.'''
        if name:
            return super().__new__(cls)

    
    def __init__(self, name):
        self.name = name # Номенклатура
        self.units_of_measurement = None # Ед. изм.
        self.initial_balance = None # Начальный остаток
        self.receipt_of_products = None # Приход
        self.movement_of_goods = None # Расход
        self.final_balance = None # Конечный остаток
        self.mark = None # Метка
        self.multiplicity = None # Кратность
        self.average_values = {} # средние значения продаж => {'17,11,': 100, '24,11,': 111, ...}
        self.declared = None # Заявлено
        self.orders = {} # Заказы {'29,11,': 50, '01,12,: 120}
        self.clients = {'медв': None, 'тк': None, 'атпр': None, 'пудп': None}
        self.comments = None


    def get_columns(self):
        return self.__dict__


    def __eq__(self, obj):
        print(f'{obj.__class__.__name__}')
        if obj.__class__.__name__ == 'Row':
            return self.name == obj.name
        return self.name == obj


    def __str__(self):
        return self.name


class Table:
    def __init__(self):
        self.columns = [
            'Номенклатура', 'Ед. изм.', 'Начальный остаток', 'Приход', 'Расход', 'Конечный остаток',
            'метка', 'крат', 'ср', 'заяв', 'разн', {'заказ': None}, #TODO
        ]




if __name__ == '__main__':
    print(Row('test'))
    print(Row())
    r1 = Row('TEST')
    print(r1.get_columns())
    r1.name = 'Obj'
    print(r1 == 'Obj')
    data = [r1]
    r2 = Row('TEST_2')
    data.append(r2)
    r2.name = 'Ok'
    print(data)
    print('Obj' in data)
    print(r1)
    print(data.index('Obj'), data.index('Ok'))
    print(r1 == r2)
    r3 = Row('Test_3')
    r3.name = 'Obj'
    print(r1 == r3)
    
