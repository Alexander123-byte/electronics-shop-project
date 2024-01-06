from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"Phone({self.name!r}, {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        """
        Магический метод, который позволяет сложить экземпляр класса
        с произвольным типом данных
        :param other: принимает остаток товара Phone
        :return: Вывод общего количества товара
        """
        if isinstance(other, Phone):
            return int(self.quantity) + int(other.quantity)
        else:
            raise TypeError("Нельзя сложить классы 'Phone' и чем-то другим.")
