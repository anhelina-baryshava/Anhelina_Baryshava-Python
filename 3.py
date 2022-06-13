m = list(map(int, input('Введите числа через пробел:').split()))
for i in m:
    if i % 3 == 0:
        print(i)
