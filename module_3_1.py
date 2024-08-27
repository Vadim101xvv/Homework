
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count_calls
def string_info(s):
    return len(s), s.upper(), s.lower()

@count_calls
def is_contains(s, lst):
    return s.lower() in [x.lower() for x in lst]

# Пример использования
print(string_info("Hello"))
print(string_info.calls) # Выводит количество вызовов функции string_info

print(is_contains("apple", ["Banana", "Orange", "Apple"]))
print(is_contains.calls) # Выводит количество вызовов функции is_contains