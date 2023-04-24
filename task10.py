# Задача 10:
#  На столе лежат n монеток. Некоторые из них лежат вверх решкой, а
# некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же
# стороной. Выведите минимальное количество монет, которые нужно
# перевернуть.

import random

n_coins = int (input("enter number of coins: "))
coins_list = []

for i in range (n_coins):
    c= random.randint(0,1)
    coins_list.append(c)
print (coins_list)
count_heads = 0 # орел
count_tails = 0 # решка
for c in coins_list:
    if c==0:
        count_tails+=1
    else:
        count_heads+=1
if count_tails > count_heads:
    print(count_heads)
else:
    print(count_tails)