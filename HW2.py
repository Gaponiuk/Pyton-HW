# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# НЕОБЯЗАТЕЛЬНО Попробовать решить не переводя числа в строку
# Пример:
# 6782 -> 23
# 0,56 -> 11

n = int(input("Введите число:"))
summ = 0
while(n > 0):
    Num = n % 10
    summ = summ + Num
    n = n//10
print("Сумма цифр равна:", summ)