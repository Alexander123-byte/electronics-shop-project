from src.keyboard import Keyboard


def test_keyboard_creation():
    """
    Тестирование создания объекта Keyboard.

    Проверяет, что объект Keyboard создается корректно.
    """
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"


def test_keyboard_default_language():
    """
    Тестирование языка клавиатуры по умолчанию.

    Проверяет, что у новой клавиатуры язык по умолчанию - EN.
    """
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb.language) == "EN"


def test_keyboard_change_language():
    """
    Тестирование смены языка клавиатуры.

    Проверяет, что метод change_lang() корректно меняет язык клавиатуры
    с EN на RU и обратно.
    """
    kb = Keyboard('Dark Project KD87A', 9600, 5)

    kb.change_lang()
    assert str(kb.language) == "RU"

    kb.change_lang()
    assert str(kb.language) == "EN"


# def test_keyboard_set_language():
# """
# Тестирование установки языка клавиатуры.

# Проверяет, что у клавиатуры нет сеттера для языка и ожидает
# AttributeError при попытке установки языка напрямую.
# """
# kb = Keyboard('Dark Project KD87A', 9600, 5)

# if hasattr(kb, 'language') and hasattr(kb.language, '__set__'):
# try:
# kb.language == 'CH'
# except AssertionError as e:
# assert "can t set attribute" in str(e)
# else:
# assert False, "Language setter not available"
