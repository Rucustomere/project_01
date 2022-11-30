# Задача 2
# Создайте список "города" с именами любых городов
# Количество элементов в списке "города" не меньше 3!

# Создайте список списков населения перечисленных городов

# Выведите на консоль население второго города в списке в формате
# Население Москвы - ХХ человек

# Выведите на консоль общий размер населения перечисленных городов как сумму населения всех городов
# Итого размер населения - ХХ человек

# Вариант 1, с помощью обработки строк
sities = 'Москва, Новосибирск, Казань, Екатеринбург, Омск'
population = '12635, 1621, 1259, 1493, 1126'
pop = population.split(',')
allpop = 0
for x in pop:
    try:
        value = int(x)
        allpop += value
    except:
        pass
print ("Население города", str.strip(sities.split(',')[1]), "-", str.strip(population.split(',')[1]), "тыс. человек")
print ("Размер населения городов ", sities , "составляет", allpop, "тыс. человек")

# Вариант 2 обработка списков
# Создаю список списков населения перечисленных городов
sitpop = [[sities.split(',')[0],population.split(',')[0]], [sities.split(',')[1],population.split(',')[1]],[sities.split(',')[2],population.split(',')[2]], [sities.split(',')[3],population.split(',')[3]], [sities.split(',')[4],population.split(',')[4]]]
#print (sitpop)
print ("Население города", sitpop[1][0], "-", sitpop[1][1], "тыс. человек")
all_pop = 0
for a in range(0, 5):
      all_pop = all_pop + int(sitpop[a][1])
print ("Итого размер населения составляет", all_pop, "тыс. человек")