import csv


class InstantiateCSVError(Exception):
    """
    Исключение, выбрасываемое при ошибке в процессе инстанциации из CSV файла.
    """


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param id: Способ создания уникального id для подсчета экземпляров класса
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.id = len(Item.all) + 1
        Item.all.append(self)

    def __repr__(self):
        return f'Item({self.name!r}, {self.price}, {self.quantity})'

    def __str__(self):
        return f'{self.name}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            self.__name = value[:10]
        self.__name = value

    @classmethod
    def instantiate_from_csv(cls,
                             filename='C:/Users/User/PycharmProjects/sky-python/electronics-shop-project/src/items.csv') -> None:
        """
        Создает экземпляры класса Item на основе данных, считанных из CSV-файла.

        :param filename: Путь к CSV-файлу с данными. По умолчанию, используется файл 'items.csv'.
        :type filename: str
        :raises FileNotFoundError: Если файл не найден.
        :raises InstantiateCSVError: Если файл поврежден (например, отсутствует колонка или данные).
        """
        try:
            Item.all.clear()
            with open(filename, newline='', encoding='windows-1251') as file:
                reader = csv.DictReader(file, delimiter=",")

                # Проверяем, что хотя бы одна строка данных присутствует в файле
                row = next(reader, None)
                if row is None:
                    raise InstantiateCSVError("Файл item.csv поврежден. Отсутствуют данные.")

                # Проверяем наличие необходимых колонок
                if 'name' not in row or 'price' not in row or 'quantity' not in row:
                    raise InstantiateCSVError("Файл item.csv поврежден. Недостаточно колонок данных.")

                # Продолжаем считывание данных
                for row in reader:
                    name = row.get('name')
                    price = row.get('price')
                    quantity = row.get('quantity')

                    cls(name, float(price), int(quantity))
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")

    @staticmethod
    def string_to_number(s):
        try:
            return int(float(s))
        except ValueError:
            return None

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        # В данном случае скидка 20%
        Item.pay_rate = 0.8
        self.price *= self.pay_rate

    def __add__(self, other):
        """
        Магический метод, который позволяет сложить экземпляр класса
        с произвольным типом данных
        :param other: Принимает остаток товара в магазине
        :return: Вывод общего количества товара
        """
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Unsupported operand type. You can only add Item instances.")


if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)
