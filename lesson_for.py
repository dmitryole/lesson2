from pprint import pprint  # визуально форматирует вывод
# Числовая последовательность 0+1+...i+n
'''
for number in range(3):
    print(f'Номер {number}')
'''
# Разбиение слова на буквы
'''
for letter in 'python':
    print(letter.upper())
'''
# Длина слова в фразе my_string
'''
my_string = 'Привет я учу python'
for world in my_string.split():
    print(f'Длина слова {world}: {len(world)}')
'''
# Расчет среднего значения
'''
student_scores = [3, 5, 4, 4, 2]
sum_scores = 0

for score in student_scores:
    scores = (avg_scores + score)

avg_score = sum_scores/len(student_scores)
print (avg_score)
'''
#Работа со списком словарей1
'''
stock = [
		{'name': 'iPhone 12', 'stock': 24, 'price': 65432.1,
                'discount': 25},
		{'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0,
                'discount': 10},
		{'name': '', 'stock': 18, 'price': 10000.0, 'discount': 10}
]

def discounted(price, discount, max_discount=30, phone_name=''):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError("Слишком большая максимальная скидка")
    if discount >= max_discount:
        return price
    elif 'iphone' in phone_name.lower() or not phone_name:
        return price
    else:
        return price - (price * discount / 100)
    
for phone in stock:
    phone ['price_final'] = discounted(phone['price'], phone['discount'], phone_name=phone['name'])
    
print (stock)
'''
#Работа со списком словарей2
classes = [
    {'name': '3А', 'scores': [3,4,4,5,2]},
    {'name': '3Б', 'scores': [5,5,3,2,2]},
    {'name': '3В', 'scores': [4,5,3,5,4]},
]

def count_class_avg(scores):
    sum_scores = 0
    for score in scores:
        sum_scores += score
    return sum_scores/len(scores)

school_avg_sum = 0
for one_classe in classes:
    classe_avg = count_class_avg(one_classe['scores'])
    print(f'Средняя оценка класса {one_classe["name"]}: {classe_avg}')
    school_avg_sum += classe_avg

school_avg = round(school_avg_sum/len(classes),1)
print(f'Средняя оценка по школе: {school_avg}')