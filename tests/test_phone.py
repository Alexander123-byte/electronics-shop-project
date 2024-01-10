from src.phone import Phone
import pytest


def test_number_of_sim():
    """
    Проверяет, что атрибут number_of_sim у экземпляра Phone корректно возвращает заданное количество сим-карт.

    Ожидаемое поведение:
    Создается экземпляр Phone с 2 сим-картами.
    Метод number_of_sim возвращает 2.
    """
    phone = Phone("iPhone", 999, 10, 2)
    assert phone.number_of_sim == 2


def test_set_number_of_sim():
    """
    Проверяет, что атрибут number_of_sim у экземпляра Phone корректно устанавливается новым значением.

    Ожидаемое поведение:
    Создается экземпляр Phone с 1 сим-картой.
    Устанавливается новое значение 2 сим-карты.
    Метод number_of_sim возвращает 2.
    """
    phone = Phone("Samsung", 799, 5, 1)
    phone.number_of_sim = 2
    assert phone.number_of_sim == 2


def test_repr():
    """
    Проверяет, что метод __repr__ у экземпляра Phone возвращает строку с ожидаемым форматом.

    Ожидаемое поведение:
    Создается экземпляр Phone с заданными характеристиками.
    Метод __repr__ возвращает строку в формате "Phone('Nokia', 299, 2, 1)"
    """
    phone = Phone("Nokia", 299, 2, 1)
    assert repr(phone) == "Phone('Nokia', 299, 2, 1)"


def test_str():
    """
    Проверяет, что метод __str__ у экземпляра Phone возвращает ожидаемое название телефона.

    Ожидаемое поведение:
    Создается экземпляр Phone с заданным названием.
    Метод __str__ возвращает строку с ожидаемым названием.
    """
    phone = Phone("Motorola", 199, 1, 1)
    assert str(phone) == "Motorola"


def test_add_phones():
    """
    Проверяет, что оператор + сложения экземпляров Phone корректно возвращает суммарное количество товара.

    Ожидаемое поведение:
    Создаются два экземпляра Phone с заданным количеством товара.
    Оператор + возвращает суммарное количество товара (10 + 5 = 15).
    """
    phone1 = Phone("iPhone", 999, 10, 1)
    phone2 = Phone("Samsung", 799, 5, 1)
    total_quantity = phone1 + phone2
    assert total_quantity == 15


def test_add_phone_with_different_class():
    """
    Проверяет, что при попытке сложить экземпляр Phone с объектом другого класса выбрасывается TypeError.

    Ожидаемое поведение:
    создается экземпляр Phone с заданными характеристиками.
    При попытке сложить его с числом (5) выбрасывается исключение TypeError.
    """
    phone = Phone("Nokia", 299, 2, 1)
    with pytest.raises(TypeError):
        total_quantity = phone + 5
