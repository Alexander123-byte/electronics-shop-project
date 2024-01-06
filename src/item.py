import csv


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
    def instantiate_from_csv(cls, filename='C:/Users/User/PycharmProjects/sky-python/electronics-shop-project/'
                                           'src/items.csv') -> None:
        Item.all.clear()
        with (open(filename, newline='', encoding='windows-1251') as file):
            reader = csv.DictReader(file, delimiter=",")
            for row in reader:
                name = row['name']
                price = int(row['price'])
                quantity = int(row['quantity'])
                cls(name, price, quantity)
        return cls.all

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
            return int(self.quantity) + int(other.quantity)
        else:
            raise TypeError("Нельзя сложить классы 'Item' и чем-то другим.")


if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)
