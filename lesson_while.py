'''
x = 1
while x < 5:
    print(x)
    x += 1
'''
'''
while True:
    user_say = input('Скажи что-нибудь: ')
    if user_say == 'Пока':
        print('Ну пока')
        break
    else:
        print('Сам ты {}'.format(user_say))
'''
#Задание1
'''
lists = ['Вася', 'Миша', 'Петя', 'Валера', 'Cаша', 'Даша']
while True:
    if lists.pop(0) in 'Валера':
        print('Валера найден')
        break
    else:
        print('Валера не найден')
'''
#Задание2
'''
lists = ['Вася', 'Миша', 'Петя', 'Валера', 'Cаша', 'Даша']

def find_persone(name):
    while True:
        if lists.pop(0) in name:
            print(f'{name} найден')
            break
        else:
            print(f'{name} не найден')

user_say = input('Напиши имя: ')
find_persone(user_say)
'''
#Задание3
'''
def ask_user():
    while True:
        user_say = input('Как дела: ')
        if user_say == 'Хорошо':
        break
def ask_user()
'''
#Задание4
'''
def get_answer():
    print('Ответ')

def ask_user():
    while True:
        user_say = input('Как дела: ')
        if user_say == 'Пока!':
            break
        else:
            get_answer()

ask_user()
'''