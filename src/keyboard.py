from src.item import Item
from src.language_mixin import LanguageMixin


class Keyboard(Item, LanguageMixin):
    """
    Класс для представления клавиатуры в магазине.

    Наследует функционал по хранению и изменению раскладки клавиатуры от LanguageMixin.
    """
    def __init__(self, name, price, quantity):
        """
        Создание экземпляра класса Keyboard.

        :param name: Название клавиатуры.
        :param price: Цена за единицу клавиатуры.
        :param quantity: Количество клавиатур в магазине.
        """
        super().__init__(name, price, quantity)
        self.__language = 'EN'

    @property
    def language(self):
        """
        Получение текущего языка клавиатуры.

        :return: Текущий язык (EN или RU).
        """
        return self.__language

    def change_lang(self):
        """
        Изменение языка клавиатуры.

        Меняет язык с EN на RU и обратно.
        """
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
