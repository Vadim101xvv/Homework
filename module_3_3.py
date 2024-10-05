def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Часть 1: Вызовы функции с разным количеством аргументов

print_params()  # Вывод: 1 строка True
print_params(10)  # Вывод: 10 строка True
print_params(10, 'другая строка')  # Вывод: 10 другая строка True
print_params(10, 'другая строка', False)  # Вывод: 10 другая строка False

# Проверка работы с именованными параметрами
print_params(b=25)  # Вывод: 1 25 True
print_params(c=[1, 2, 3])  # Вывод: 1 строка [1, 2, 3]

# Часть 2: Распаковка параметров

values_list = [42, 'пример', False]
values_dict = {'a': 99, 'b': 'тест', 'c': None}

print_params(*values_list)  # Вывод: 42 пример False
print_params(**values_dict)  # Вывод: 99 тест None

# Часть 3: Распаковка + отдельные параметры

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)  # Вывод: 54.32 Строка 42