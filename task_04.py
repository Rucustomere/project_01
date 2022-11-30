# Задача 4
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
# Для того, чтобы задавать случайные значения, используйсте модуль random
# import random 

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
import random

random_n1 = random.randint(0, 8)
random_n2 = random.randint(0, 8)
random_n3 = random.randint(0, 8)
#print(random_n1, random_n2, random_n3)
a = my_favorite_songs [random_n1][1]
b = my_favorite_songs [random_n2][1]
c = my_favorite_songs [random_n3][1]
#summa_song = a+b+c
summa_song = round((a+b+c), 2)
print(" Три песни:", my_favorite_songs [random_n1][0],",", my_favorite_songs [random_n2][0], ",", my_favorite_songs [random_n3][0], "-", "звучат", summa_song, "минут")