# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# НЕОБЯЗАТЕЛЬНО Попробовать решить не переводя числа в строку
# Пример:
# 6782 -> 23
# 0,56 -> 11

# n = int(input("Введите число:"))
# summ = 0
# while(n > 0):
#     Num = n % 10
#     summ = summ + Num
#     n = n//10
# print("Сумма цифр равна:", summ)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда (1, 1*2, 1*2*3, 1*2*3*4) 

# n = int(input('input N: '))
# factorial = 1
# for i in range(1, n+1):
#      factorial *= i
#      print(factorial, end=' ')

# Задайте список из n чисел последовательности (1+1/n)^n
# Выведитте на экран саму последовательность и сумму элеементов этой последовательности (для проверки сумма для 4 элементов = 9,06 (примерно))

n = int(input ("Введите число" ))
lst = [round((1+1/i)**i, 3) for i in range(1, n+1)]
print('Последовательность: {lst}\nСумма: {round(sum(lst), 3)}')

# Реализуйте алгоритм перемешивания списка, без использования встроеных методов (особенно SHUFFLE, без него) 
# можно (нужно) использовать библиотеку Random


