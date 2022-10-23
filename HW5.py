# # 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"

# # my_text = 'Привет друзьяабв, меня зовут Денис Юрьевичабв, я учусь ужеабв абвнесколько месяцевабв на бизнес-аналитика'

# # def del_some_words(my_text):
# #     my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
# #     return " ".join(my_text)

# # my_text = del_some_words(my_text)
# # print(my_text)

# # 2. Создайте программу для игры с конфетами человек против человека.

# # Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# # За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# # Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# # 1. Добавьте игру против бота
# # 2. Подумайте как наделить бота 'интеллектом'
# # Оба задания обязательны

# # Игра против игрока (человека):
# # from random import randint

# # def input_dat(name):
# #     x = int(input(f"{name}, сколько конфет Вы хотите взять от 1 до 28: "))
# #     while x < 1 or x > 28:
# #         x = int(input(f"{name}, Это кол-во не удовлетворяет условям игры: "))
# #     return x


# # def p_print(name, k, counter, value):
# #     print(f"Ход сделал {name}, забрал {k}, у него {counter}. На столе {value} конфет.")

# # player1 = input("Введите имя 1 игрока: ")
# # player2 = input("Введите имя 2 игрока: ")
# # value = int(input("Сколько конфет на столе? "))
# # flag = randint(0,2) 
# # if flag:
# #     print(f"1-ый ходит {player1}")
# # else:
# #     print(f"2-ой ходит {player2}")

# # counter1 = 0 
# # counter2 = 0

# # while value > 28:
# #     if flag:
# #         k = input_dat(player1)
# #         counter1 += k
# #         value -= k
# #         flag = False
# #         p_print(player1, k, counter1, value)
# #     else:
# #         k = input_dat(player2)
# #         counter2 += k
# #         value -= k
# #         flag = True
# #         p_print(player2, k, counter2, value)

# # if flag:
# #     print(f"Выиграл {player1}")
# # else:
# #     print(f"Выиграл {player2}")

# # 3. Создайте программу для игры в 'Крестики-нолики'.

# # print("*" * 10, " Крестики-нолики для 2-х игроков ", "*" * 10)

# # board = list(range(1,10))

# # def draw_board(board):
# #    print("-" * 13)
# #    for i in range(3):
# #       print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
# #       print("-" * 13)

# # def take_input(player_token):
# #    valid = False
# #    while not valid:
# #       player_answer = input("В какую ячейку" + player_token+"? ")
# #       try:
# #          player_answer = int(player_answer)
# #       except:
# #          print("Некорректная ячейка. Вы ввели число?")
# #          continue
# #       if player_answer >= 1 and player_answer <= 9:
# #          if(str(board[player_answer-1]) not in "XO"):
# #             board[player_answer-1] = player_token
# #             valid = True
# #          else:
# #             print("Клетка занята!")
# #       else:
# #         print("Некорректная ячейка. Введите число от 1 до 9.")

# # def check_win(board):
# #    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
# #    for each in win_coord:
# #        if board[each[0]] == board[each[1]] == board[each[2]]:
# #           return board[each[0]]
# #    return False

# # def main(board):
# #     counter = 0
# #     win = False
# #     while not win:
# #         draw_board(board)
# #         if counter % 2 == 0:
# #            take_input("X")
# #         else:
# #            take_input("O")
# #         counter += 1
# #         if counter > 4:
# #            tmp = check_win(board)
# #            if tmp:
# #               print(tmp, "выиграл!")
# #               win = True
# #               break
# #         if counter == 9:
# #             print("Ничья!")
# #             break
# #     draw_board(board)
# # main(board)

# # input("Нажмите Enter для выхода!")


# # 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# # Входные и выходные данные хранятся в отдельных текстовых файлах.

# # Пример: aaaaaaabbbbbbcccccccccd => 7a6b9c1d или 11a3b7c1d => aaaaaaaaaaabbbcccccccd

# with open('file_encode.txt', 'w') as data:
#     data.write('SSSSSSSSSSSSSDDDDDDDDDDDDNNJJJJJJJNNJJJJJJJJJJJJJJJ')

# with open('file_encode.txt', 'r') as data:
#     string = data.readline()

# def rle_encode(decoded_string):
#     encoded_string = ''
#     count = 1
#     char = decoded_string[0]
#     for i in range(1, len(decoded_string)):
#         if decoded_string[i] == char:
#             count += 1
#         else:
#             encoded_string = encoded_string + str(count) + char
#             char = decoded_string[i]
#             count = 1
#             encoded_string = encoded_string + str(count) + char
#     return encoded_string


# def rle_decode(encoded_string):
#     decoded_string = ''
#     char_amount = ''
#     for i in range(len(encoded_string)):
#         if encoded_string[i].isdigit():
#             char_amount += encoded_string[i]
#         else:
#             decoded_string += encoded_string[i] * int(char_amount)
#         char_amount = ''
#     print(decoded_string)

#     return decoded_string


# with open('file_encode.txt', 'r') as file:
#     decoded_string = file.read()

# with open('file_decode.txt', 'w') as file:
#     encoded_string = rle_encode(decoded_string)
#     file.write(encoded_string)

# print('Decoded string: \t' + decoded_string)
# print('Encoded string: \t' + rle_encode(decoded_string))
# print(f'Compress ratio: \t{round(len(decoded_string) / len(encoded_string), 1)}')