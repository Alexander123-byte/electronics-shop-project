"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv
import os

from src.item import Item
from src.phone import Phone
import pytest
from src.item import Item, InstantiateCSVError


def test_total_price():
    """Тестирование расчета стоимости товара без учета скидки"""

    item1 = Item("Ноутбук", 10000.0, 20)
    item2 = Item("Смартфон", 5990.0, 35)
    item3 = Item("Наушники", 1890.0, 15)

    # Без скидки
    assert item1.calculate_total_price() == 200000.0
    assert item2.calculate_total_price() == 209650.0
    assert item3.calculate_total_price() == 28350


def test_apply_discount():
    """Тестирование расчета стоимости товара с учетом скидки"""
    # Устанавливаем свою скидку на товар в размере 20%
    Item.pay_rate = 0.8
    item1 = Item("Ноутбук", 10000.0, 20)
    item2 = Item("Смартфон", 5990.0, 35)
    item3 = Item("Наушники", 1890.0, 15)

    # Скидка 20%
    item1.apply_discount()
    item2.apply_discount()
    item3.apply_discount()

    assert item1.price == 8000.0
    assert item2.price == 4792.0
    assert item3.price == 1512.0


def test_item_name():
    item = Item('Телефон', 10000, 5)
    assert item.name == 'Телефон'

    # Установка короткого имени
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # Установка длинного имени
    item.name = 'СуперСмартфон'
    assert item.name.startswith('СуперСмарт')


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_item_repr():
    item = Item('Телефон', 10000, 5)
    assert repr(item) == "Item('Телефон', 10000, 5)"


def test_item_str():
    item = Item('Телефон', 10000, 5)
    assert str(item) == "Телефон"


def test_add_with_item():
    phone1 = Phone("iPhone", 999, 10, 1)
    item1 = Item("Смартфон", 10000, 20)
    total_quantity = item1 + phone1
    assert total_quantity == 30


def test_add_with_item_2():
    phone1 = Phone("iPhone", 999, 10, 1)
    item1 = Item("Смартфон", 10000, 20)
    total_quantity = item1 + phone1
    assert total_quantity != 10


def test_add_with_different_class():
    phone = Phone("Nokia", 299, 2, 1)
    with pytest.raises(TypeError):
        total_quantity = phone + 5
    item1 = Item("Смартфон", 10000, 20)
    with pytest.raises(TypeError):
        remaining_quantity = item1 - 5


def test_instantiate_from_csv_file_not_found():
    """
    Проверяет, что при отсутствии файла item.csv выбрасывается FileNotFoundError.
    """
    with pytest.raises(FileNotFoundError, match="Отсутствует файл item.csv"):
        Item.instantiate_from_csv(filename='nonexistent_file.csv')


def test_instantiate_from_csv_file_corrupted():
    """
    Проверяет, что при повреждении файла item.csv выбрасывается InstantiateCSVError.
    """
    # Создаем временный файл с отсутствующей колонкой
    filename = 'corrupted_file.csv'
    with open(filename, 'w', newline='', encoding='windows-1251') as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(['name', 'price'])  # Отсутствует колонка 'quantity'

    with pytest.raises(InstantiateCSVError, match="Файл item.csv поврежден. Отсутствуют данные.") as info:
        Item.instantiate_from_csv(filename='corrupted_file.csv')

    # Удаляем временный файл
    os.remove(filename)


def test_instantiate_from_csv_file_empty():
    """
    Проверяет, что при отсутствии данных в файле item.csv выбрасывается InstantiateCSVError.
    """
    # Создаем временный файл без строк данных
    filename = 'empty_file.csv'
    with open(filename, 'w', newline='', encoding='windows-1251') as file:
        writer = csv.writer(file, delimiter=",")
        # Не добавляем строки данных

    with pytest.raises(InstantiateCSVError, match="Файл item.csv поврежден. Отсутствуют данные.") as info:
        Item.instantiate_from_csv(filename='empty_file.csv')

    # Удаляем временный файл
    os.remove(filename)