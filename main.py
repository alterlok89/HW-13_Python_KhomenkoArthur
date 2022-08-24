# Задание 1

# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса:
# название модели, год выпуска, производителя, объем двигателя, цвет машины, цену.
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
# lines = [line for line in open('task3_text1.txt', 'r')]

# class auto():
#     def __init__(self, model, year, manufact, engine, color, price):
#         self.__model = model
#         self.__year = year
#         self.__manufact = manufact
#         self.__engine = engine
#         self.color = color
#         self.price = price
#
#     def get_model(self):
#         return self.__model
#
#     def set_model(self, model):
#         # список моделей взяты из файла:
#         model_list = [line.replace('\n', '').lower() for line in open('model.txt', 'r')]
#         if model.lower() in model_list:
#             self.__model = model
#         else:
#             print('Не вверно введена модель машины!')
#
#     def get_year(self):
#         return self.__year
#
#     def set_year(self, year):
#         if str(year).isdigit():
#             if 1950 < int(year) < 2022:
#                 self.__year = year
#             else:
#                 print('Не верно установлен год выпуска машины!')
#
#     def get_manufact(self):
#         return self.__manufact
#
#     def set_manufact(self, manufact):
#         if manufact == 'AUDI':
#             self.__manufact = manufact
#         else:
#             print('Нельзя изменить производителя машины!')
#
#     def get_engine(self):
#         return self.__engine
#
#     def set_engine(self, engine):
#         if float(engine):
#             if 0 < float(engine) < 10:
#                 self.__engine = float(engine)
#             else:
#                 print('Не верно введен объем двигателя машины!')
#
#     def __str__(self):
#         return (f'Модель: {self.__model}\n'
#                 f'Год выпуска: {self.__year}\n'
#                 f'Производитель: {self.__manufact}\n'
#                 f'Объем двигателя: {self.__engine}\n'
#                 f'Цвет: {self.color}\n'
#                 f'Цена: {self.price} $')
#
#     def change_color(self, new_color):
#         # списокофициальных цветов производителя взяты из файла:
#         color_list = [line.replace('\n', '').lower() for line in open('color.txt', 'r')]
#         if new_color.lower() in color_list:
#             self.color = new_color
#         else:
#             print('Не верно указан цвет машины! Цвет не изменен!')
#
#     def change_price(self, new_price):
#         if new_price.isdigit():
#             if int(new_price) > 0:
#                 self.price = new_price
#             else:
#                 print('Не верно указана цена машины! Цена не изменена!')
#         else:
#             print('Не верно указана цена машины! Цена не изменена!')
#
#
# obj = auto('TT quattro sport', 2020, 'AUDI', 2.2, 'Atlas Gray Metallic Clearcoat', 15000)
# # print(obj)
#
# # obj.set_year('1990')
# # print(obj.get_year())
# # obj.set_manufact('100')
# # print(obj.get_manufact())
# # obj.change_price('100')
# # print(obj.price)
# # obj.change_color('Brilliant Red')
# # print(obj.color)
# # print(obj)
# # obj.set_engine(1.5)
# # print(obj.get_engine())
#
# while True:
#     # find_list = ('find', 'model', 'year', 'manufact', 'engine', 'color', 'price')
#     menu = ('1. Вывести все данные об автомобиле',
#             '2. Найти данные машины',
#             '3. Изменить данные машины',
#             '4. Выход из программы')
#     print('-'*80)
#     for i in menu:
#         print(i)
#     print('-'*80)
#     change = int(input('Выберите действие которое вы хотите выполнить: '))
#     print()
#     if change == 1:
#         print('-'*80)
#         print(f'Данные об автомобиле:\n\n'
#               f'{obj}')
#         print('-'*80)
#     elif change == 2:
#         find = ''
#         while find != 'end':
#             print('-'*80)
#             print('model - Найти данные о модели машины\n'
#                   'year - Найти данные о годе производства машины\n'
#                   'manufact - Найти данные о производителе машины\n'
#                   'engine - Найти данные об объеме двигателя машины\n'
#                   'color - Найти данные о цвете машины\n'
#                   'price - Найти данные о цене машины\n'
#                   'end - Завершить поиск')
#             print('-'*80)
#             find = input('Какой параметр необходимо найти: ')
#             if find == 'model':
#                 model = obj.get_model()
#                 print(f'Модель автомобиля: {model}\n')
#             elif find == 'year':
#                 year = obj.get_year()
#                 print(f'Год выпуска автомобиля: {year}\n')
#             elif find == 'manufact':
#                 manufact = obj.get_manufact()
#                 print(f'Производитель автомобиля: {manufact}\n')
#             elif find == 'engine':
#                 engine = obj.get_engine()
#                 print(f'Объем двигателя автомобиля: {engine}\n')
#             elif find == 'color':
#                 color = obj.color
#                 print(f'Цвет автомобиля: {color}\n')
#             elif find == 'price':
#                 price = obj.price
#                 print(f'Цена автомобиля: {price } $\n')
#
#     elif change == 3:
#         replace = ''
#         while replace != 'end':
#             print('-'*80)
#             print('model - Изменить данные о модели машины\n'
#                   'year - Изменить данные о годе производства машины\n'
#                   'manufact - Изменить данные о производителе машины\n'
#                   'engine - Изменить данные об объеме двигателя машины\n'
#                   'color - Изменить данные о цвете машины\n'
#                   'price - Изменить данные о цене машины\n'
#                   'end - Завершить поиск')
#             print('-'*80)
#             replace = input('Какой параметр необходимо изменить: ')
#             if replace == 'model':
#                 obj.set_model(input('Введите модель машины: '))
#                 print(f'Модель автомобиля: {obj.get_model()}\n')
#             elif replace == 'year':
#                 obj.set_year(input('Введите год выпуска машины: '))
#                 print(f'Год выпуска автомобиля: {obj.get_year()}\n')
#             elif replace == 'manufact':
#                 obj.set_manufact(input('Введите производителя машины: '))
#                 print(f'Производитель автомобиля: {obj.get_manufact()}\n')
#             elif replace == 'engine':
#                 obj.set_engine(input('Введите объем двигателя машины: '))
#                 print(f'Объем двигателя автомобиля: {obj.get_engine()}\n')
#             elif replace == 'color':
#                 obj.change_color(input('Введите цвет машины: '))
#                 print(f'Цвет автомобиля: {obj.color}\n')
#             elif replace == 'price':
#                 obj.change_price(input('Введите цену машины: '))
#                 print(f'Цена автомобиля: {obj.price} $\n')
#
#     elif change == 4:
#         print('-'*80)
#         print(f'Данные об автомобиле в конце работы:\n\n'
#               f'{obj}')
#         print('-'*80)
#         break

# Задание 2

# Реализуйте класс «Книга».
# Необходимо хранить в полях класса:
# название книги, год выпуска, издателя, жанр, автора, цену.
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса

class book():
    def __init__(self, name, year, publisher, genre, author, price):
        self.__name = name
        self.__year = year
        self.publisher = publisher
        self.__genre = genre
        self.__author = author
        self.price = price

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_year(self):
        return self.__year

    def set_year(self, year):
        if str(year).isdigit():
            if 1850 < int(year) < 2022:
                self.__year = year
            else:
                print('Не верно указан год выпуска книги!')

    def change_publisher(self, new_publisher):
        self.publisher = new_publisher

    def get_genre(self):
        return self.__genre

    def set_genre(self, genre):
        # списокофициальных жанров взяты из файла:
        genre_list = [line.replace('\n', '').lower() for line in open('genre.txt', 'r', encoding="utf8")]
        if genre.lower() in genre_list:
            self.__genre = genre
        else:
            print('Не вверно введен жанр книги! Жанр не изменен!')

    def get_author(self):
        return self.__author

    def change_price(self, new_price):
        if new_price.isdigit():
            if int(new_price) > 0:
                self.price = new_price
            else:
                print('Не верно указана цена книги! Цена не изменена!')
        else:
            print('Не верно указана цена книги! Цена не изменена!')

    def __str__(self):
        return (f'Название книги: {self.__name}\n'
                f'Год выпуска: {self.__year}\n'
                f'Издательство: {self.publisher}\n'
                f'Жанр: {self.__genre}\n'
                f'Автор: {self.__author}\n'
                f'Цена: {self.price} грн.')


obj_book = book('Изучаем Java', 2021, 'ЭКСМО', 'Учебная книга', 'Кэти Сьерра и Берт Бейтс', 1000)
# print(obj_book)
# print(obj_book.__dir__())
# print(obj_book.get_name())

# genre_list = [line.replace('\n', '').lower() for line in open('genre.txt', 'r', encoding="utf8")]
# print(genre_list)

while True:
    # find_list = ('find', 'name', 'year', 'publisher', 'genre', 'author', 'price')
    menu = ('1. Вывести все данные о книге',
            '2. Найти данные книги',
            '3. Изменить данные книги',
            '4. Выход из программы')
    print('-'*80)
    for i in menu:
        print(i)
    print('-'*80)
    change = int(input('Выберите действие которое вы хотите выполнить: '))
    print()
    if change == 1:
        print('-'*80)
        print(f'Данные о книге:\n\n'
              f'{obj_book}')
        print('-'*80)
    elif change == 2:
        find = ''
        while find != 'end':
            print('-'*80)
            print('name - Найти названиекниги \n'
                  'year - Найти год выхода книги\n'
                  'publisher - Найти издательство книги\n'
                  'genre - Найти жанр книги\n'
                  'author - Найти автора книги\n'
                  'price - Найти цену книги\n'
                  'end - Завершить поиск')
            print('-'*80)
            find = input('Какой параметр необходимо найти: ')
            if find == 'name':
                name = obj_book.get_name()
                print(f'Название книги: {name}\n')
            elif find == 'year':
                year = obj_book.get_year()
                print(f'Год выхода книги: {year}\n')
            elif find == 'publisher':
                publisher = obj_book.publisher
                print(f'Издательство книги: {publisher}\n')
            elif find == 'genre':
                genre = obj_book.get_genre()
                print(f'Объем двигателя автомобиля: {genre}\n')
            elif find == 'author':
                author = obj_book.get_author()
                print(f'Автор книги: {author}\n')
            elif find == 'price':
                price_book = obj_book.price
                print(f'Цена книги: {price_book} грн.\n')
    elif change == 3:
        replace = ''
        while replace != 'end':
            print('-'*80)
            print('name - Найти названиекниги \n'
                  'year - Найти год выхода книги\n'
                  'publisher - Найти издательство книги\n'
                  'genre - Найти жанр книги\n'
                  'author - Найти автора книги\n'
                  'price - Найти цену книги\n'
                  'end - Завершить поиск')
            print('-'*80)
            replace = input('Какой параметр необходимо изменить: ')
            if replace == 'name':
                obj_book.set_name(input('Введите новое название книги: '))
                print(f'Название книги: {obj_book.get_name()}\n')
            elif replace == 'year':
                obj_book.set_year(input('Введите год выхода книги: '))
                print(f'Год выхода книги: {obj_book.get_year()}\n')
            elif replace == 'publisher':
                publisher = obj_book.change_publisher(input('Введите новое издательство: '))
                print(f'Издательство книги: {publisher}\n')
            elif replace == 'genre':
                obj_book.set_genre(input('Введите жанр книги: '))
                print(f'Жанр книги: {obj_book.get_genre()}\n')
            elif replace == 'author':
                print('Автора книги не изменить!')
                author = obj_book.get_author()
                print(f'Автор книги: {author}\n')
            elif replace == 'price':
                obj_book.change_price(input('Введите цену книги: '))
                print(f'Цена автомобиля: {obj_book.price} грн.\n')

    elif change == 4:
        print('-'*80)
        print(f'Данные о книге в конце работы:\n\n'
              f'{obj_book}')
        print('-'*80)
        break
