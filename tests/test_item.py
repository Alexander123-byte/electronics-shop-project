"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item


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
