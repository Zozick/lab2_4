def fibonacci(n):
    """
    Возвращает список из n чисел Фибоначчи
    Граничные значения: n=0, n=1, n=2
    """
    if n < 0:
        raise ValueError("n не может быть отрицательным")
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib


def bubble_sort(numbers):
    """
    Сортирует список чисел методом пузырька
    Возвращает отсортированную копию
    """
    if not isinstance(numbers, list):
        raise TypeError("Должен быть список")

    arr = numbers.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def eratosthenes(n):
    """
    Находит все простые числа до n
    Граничное значение: n=2
    """
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
    return primes
