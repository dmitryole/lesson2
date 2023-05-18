
import ephem
#import datetime

mars = ephem.Mars('2000/01/01')
constellation = ephem.constellation(mars)
print(constellation)

#Тестирование кода для бота
"""
def get_planet(user_message):
    try:
        #Получаем now из библиотеки datetime, возможно в переменая context седеожит дату
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        #Вытаскиваем название планеты из сообщения
        name_planet = (user_message.split())[1].capitalize()
        #Присваиваем переменую name_planet в атрибут
        ephem_name_planet= getattr(ephem, name_planet)
        #Получаем координаты планеты
        planet = ephem_name_planet(now)
        #Запрос созвездия
        constellation = (ephem.constellation(planet))[1]
        print(f'{name_planet} in the constellation {constellation}')
    except AttributeError:
        print("Check planet name")

get_planet('/planet moon')
"""