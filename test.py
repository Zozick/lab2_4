
import pytest
from task2_4 import fibonacci, bubble_sort, eratosthenes


# Тесты для чисел Фибоначчи
def test_fibonacci():
    # Корректные данные
    assert fibonacci(0) == []  # граничное значение
    assert fibonacci(1) == [0]  # граничное значение
    assert fibonacci(2) == [0, 1]  # граничное значение
    assert fibonacci(5) == [0, 1, 1, 2, 3]  # обычный случай

    # Некорректные данные
    with pytest.raises(ValueError):
        fibonacci(-1)  # отрицательное число

    # Некорректные типы
    with pytest.raises(TypeError):
        fibonacci(5.5)  # дробное число
    with pytest.raises(TypeError):
        fibonacci("5")  # строка
    with pytest.raises(TypeError):
        fibonacci([5])  # список


# Тесты для сортировки
def test_bubble_sort():
    # Корректные данные
    assert bubble_sort([]) == []  # пустой список
    assert bubble_sort([5]) == [5]  # один элемент
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]  # обычный случай
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]  # обратный порядок
    assert bubble_sort([3.5, 1.2, 2.8]) == [1.2, 2.8, 3.5]  # дробные числа

    # Проверка что исходный список не меняется
    original = [3, 1, 2]
    sorted_arr = bubble_sort(original)
    assert original == [3, 1, 2]

    # Некорректные типы для списка
    with pytest.raises(TypeError):
        bubble_sort("не список")  # строка вместо списка
    with pytest.raises(TypeError):
        bubble_sort(123)  # число вместо списка

    # Некорректные типы элементов списка
    with pytest.raises(TypeError):
        bubble_sort([1, 2, "текст"])  # строка в списке
    with pytest.raises(TypeError):
        bubble_sort([1, [2], 3])  # список в списке


# Тесты для решета Эратосфена
def test_eratosthenes():
    # Корректные данные
    assert eratosthenes(2) == [2]  # граничное значение
    assert eratosthenes(10) == [2, 3, 5, 7]  # обычный случай
    assert eratosthenes(1) == []  # n < 2

    # Некорректные данные (функция возвращает [] вместо ошибки)
    assert eratosthenes(0) == []
    assert eratosthenes(-5) == []

    # Некорректные типы
    with pytest.raises(TypeError):
        eratosthenes(10.5)  # дробное число
    with pytest.raises(TypeError):
        eratosthenes("20")  # строка


# Дополнительные тесты на граничные значения
def test_boundary_values():
    # Граничные значения для Фибоначчи
    assert fibonacci(3) == [0, 1, 1]

    # Граничные значения для сортировки
    assert bubble_sort([1, 1]) == [1, 1]  # одинаковые элементы
    assert bubble_sort([-1, -3, -2]) == [-3, -2, -1]  # отрицательные числа

    # Граничные значения для решета
    assert eratosthenes(3) == [2, 3]
    assert eratosthenes(13) == [2, 3, 5, 7, 11, 13]  # включая границу