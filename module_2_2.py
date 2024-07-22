print('Введите 3 любых числа:')
a = input('Введите число:')
b = input('Введите число:')
c = input('Введите число:')
if a == b and b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)