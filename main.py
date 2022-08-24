# Задание 1

# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса:
# название модели, год выпуска, производителя, объем двигателя, цвет машины, цену.
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
# lines = [line for line in open('task3_text1.txt', 'r')]

class auto():
    def __init__(self, model, year, manufact, engine, color, price):
        self.__model = model
        self.__year = year
        self.__manufact = manufact
        self.__engine = engine
        self.color = color
        self.price = price

    def get_model(self):
        return self.__model

    def set_model(self, model):
        # список моделей взяты из файла:
        model_list = [line.replace('\n', '').lower() for line in open('model.txt', 'r')]
        if model.lower() in model_list:
            self.__model = model
        else:
            print('Не вверно введена модель машины!')

    def get_year(self):
        return self.__year

    def set_year(self, year):
        if str(year).isdigit():
            if 1950 < year < 2022:
                self.__year = year
            else:
                print('Не верно установлен год выпуска машины!')

    def get_manufact(self):
        return self.__manufact

    def set_manufact(self, manufact):
        if manufact == 'AUDI':
            self.__manufact = manufact
        else:
            print('Нельзя изменить производителя машины!')

    def __str__(self):
        return (f'Модель: {self.__model}\n'
                f'Год выпуска: {self.__year}\n'
                f'Производитель: {self.__manufact}\n'
                f'Объем двигателя: {self.__engine}\n'
                f'Цвет: {self.color}\n'
                f'Цена: {self.price} $')

    def change_color(self, new_color):
        # списокофициальных цветов производителя взяты из файла:
        color_list = [line.replace('\n', '').lower() for line in open('color.txt', 'r')]
        if new_color.lower() in color_list:
            self.color = new_color
        else:
            print('Не верно указан цвет машины! Цвет не изменен!')

    def change_price(self, new_price):
        if new_price.isdigit():
            if int(new_price) > 0:
                self.price = new_price
            else:
                print('Не верно указана цена машины! Цена не изменена!')
        else:
            print('Не верно указана цена машины! Цена не изменена!')


obj = auto('TT quattro sport', 2020, 'AUDI', 2.2, 'Atlas Gray Metallic Clearcoat', 15000)
# print(obj)

# obj.set_manufact('100')
# print(obj.get_manufact())
# obj.change_price('100')
# print(obj.price)
# obj.change_color('Brilliant Red')
# print(obj.color)
# print(obj)

while True:
    menu = ('1. Вывести все данные об автомобиле',
            '2. Найти данные машины',
            '3. Изменить данные машины',
            '4. Выход из программы')
    print('-------------------------------------------------------------------------------')
    for i in menu:
        print(i)
    print('-------------------------------------------------------------------------------')
    change = int(input('Выберите действие которое вы хотите выполнить: '))
    print()
    if change == 1:
        print(auto())
    elif change == 2:
        car.set_data()
        print(car)
    elif change == 3:
        print(car)
    elif change == 4:
        break
