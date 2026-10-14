# Спроси N, посчитай сумму 1+2+...+N циклом и выеди ответ в принте.
n = int(input("Введи число: "))
total = 0
for i in range(1, n + 1):
    total += i
    if i > 0:
        total += 1
print(111)
