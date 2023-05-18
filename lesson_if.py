"""
balance = 100
price = 50
in_stock = 0

print (bool(balance > price))
print (bool(in_stock))

if balance > price and in_stock:
    print('Одобряем оплату покупки')
elif not in_stock:
    print('Товара нет в наличии')
else:
    print('Пожалуйста, пополните баланс!')
"""
"""
def check_weather(temperature):
    if temperature < 0:
        return 'На улице холодно'
    elif 0 <= temperature < 15:
        return 'На улице прохладно'
    elif 15 <= temperature < 25:
        return 'На улице тепло'
    else:
        return 'На улице жарко'

print(check_weather(-10)) #"На улице холодно"
print(check_weather(8)) #"На улице прохладно"
print(check_weather(20)) #"На улице тепло"
print(check_weather(30)) #"На улице жарко"
print(check_weather(25)) #"На улице жарко"
"""

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
    

new_price = discounted(100000, 10, phone_name='iPhone 12')
print(new_price) #100000

new_price = discounted(40000, 20, phone_name='Samsung')
print(new_price) #32000

new_price = discounted(5000, 20)
print(new_price) #5000