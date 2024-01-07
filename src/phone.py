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
        if isinstance(other, Item) or isinstance(other, Phone):
            total_quantity = self.quantity + other.quantity
            total_number_of_sim = self.number_of_sim
            if isinstance(other, Phone):
                total_number_of_sim += other.number_of_sim

            if total_number_of_sim <= 0 or not isinstance(total_number_of_sim, int):
                raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

            return total_quantity
        else:
            raise TypeError("Unsupported operand type. You can only add Phone or Item instances.")

        # if isinstance(other, Item) or isinstance(other, Phone):
            # return self.quantity + other.quantity
        # else:
            # raise TypeError("Unsupported operand type. You can only add Phone or Item instances.")
