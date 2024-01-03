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

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            self.__name = value[:10]
            print("Длина наименования товара превышает 10 символов.")
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


# Пример использования класса
# if __name__ == "__main__":
    # item1 = Item("Ноутбук", 10000.0, 20)
    # item2 = Item("Смартфон", 5990.0, 35)
    # item3 = Item("Наушники", 1890, 15)

    # print(f"В нашем магазине электроники в наличии {len(Item.all)} товаров!\n")

    # print(f"Товар {item1.name} с полной стоимостью = {item1.calculate_total_price()}")
    # print(f"Товар {item2.name} с полной стоимостью = {item2.calculate_total_price()}")
    # print(f"Товар {item3.name} с полной стоимостью = {item3.calculate_total_price()}\n")

    # item1.apply_discount()
    # item2.apply_discount()
    # item3.apply_discount()

    # print(f"Товар {item1.name} с учетом скидки = {item1.price}")
    # print(f"Товар {item2.name} с учетом скидки = {item2.price}")
    # print(f"Товар {item3.name} с учетом скидки = {item3.price}")

if __name__ == '__main__':
    Item.instantiate_from_csv()

    for item in Item.all:
        print(item.name, item.price, item.quantity)
