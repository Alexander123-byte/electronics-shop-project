class LanguageMixin:
    """
    Миксин для добавления фукционала по хранению и изменению раскладки клавиатуры.

    Подмешивается в цепочку наследования класса Keyboard.
    """
    def __init__(self):
        """
        Инициализация миксина.

        Устанавливает язык по умолчанию - английский (EN).
        """
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
