n = int(input("Введите число от 3 до 20: "))
result = ""

for i in range(1, 21):
    for j in range(1, 21):
        if i < j and n % (i + j) == 0:
            result += str(i) + str(j)


print(result)