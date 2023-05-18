import random
'''
def cup_cake(people):
    try:
        z = 1 / people
        print(f'Каждый получит {z} пирога')
    except (ZeroDivisionError, TypeError):
      print(f'Не могу поделить!')
    
    
while True:
    p = random.randint(1, 10)
    cup_cake(p)

'''
#Задание 1
'''
def get_answer():
    print('Ответ')

def ask_user():
    while True:
        try:    
            user_say = input('Как дела: ')
            if user_say == 'Пока!':
                break
            else:
                get_answer()
        except (KeyboardInterrupt):
            print(f'\nПока!')
            break

ask_user()
'''
#Задание 2

def discounted(price, discount, max_discount = 20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
        if max_discount >= 100:
            raise ValueError('Максимальная скидка не должна быть больше 100')
        if discount >= max_discount:
            price_with_discount = price
        else:
            price_with_discount = price - (price * discount / 100)
        return(price_with_discount)
    except (TypeError):
        print('Ошибка в типе данных')
    except (ValueError):
        print('Ошибка в значении')

print(discounted(100, 2))
