"""
ТЗ:
По данным введенным пользователем вычислить, сможет он купить выбранный им товар или нет.
Если товар в списке отсутствует - NOT OK
__________
Входные данные: название товара,кол-во товара, наличные
Реализовать 2+ функциями
Выходные данные: словарь состящий из:
{названия товара как ключ:кол-во, следующий элемент - потраченная сумма - ключ, значение сумма}
"""
# Моя версия
# data = {
#     'glock.20': 2000,
#     'usp': 2500,
#     'fs': 3467,
#     'deagle': 5000,
#     'p92': 4000,
#     'colt': 90000,
#     'magnum': 6000,
#     'p90': 10000,
#     'mp7': 11000,
#     'uzi': 12000,
#     'mp5': 14000,
#     'm16': 20000,
#     'ak-47': 19000,
#     'm416': 24000,
#     'famas': 21000,
#     'AWM': 30000,
#     'Dragunov': 31000,
#     'Barett': 50000,
#     'RPG': 100000,
#     'Topol-M': 2000000
# }
#
# dict1 = {}
#
#
# def count_money(price, weapon_q, users_money):
#     # price = data[weapon]
#     price = data[weapon]
#     return users_money - price * weapon_q
#
#
# weapon = 'AWM'
# price = data[weapon]
#
#
# def buyer_dt(weapon_name, weapon_q, users_money):
#     summ_price = price * weapon_q
#     payback = count_money(data[weapon_name], weapon_q, users_money)
#     if weapon in data:
#         if weapon_name == weapon:
#             print('Цена товара:', data[weapon])
#         else:
#             print('Такого оружия нет')
#
#     if price * weapon_q <= users_money:
#         print('Спасибо за покупку')
#         print('Ваша сдача:', payback)
#         dict1[weapon] = weapon_q,
#         dict1['Потрачено:'] = summ_price
#         print(dict1)
#     else:
#         print('Недостаточно средств')
#
#
# buyer_dt('AWM', 5, 150001)


# weapon = input()
# quantity = int(input())
# money = int(input())
# def count_payback(price,quantity,money):
#     payback = quantity * price
#     if money >= payback:
#         return money - payback
#     else:
#         return 'Недостаточно средств'
# def shop(weapon_name,quantity,money):
#     if weapon_name in data:
#         price = data[weapon_name]
#         payback = count_payback(price,quantity,money)
#         if isinstance(payback,int):
#             result = {weapon_name:quantity,'total_sum':price*quantity}
#         else:
#             result = payback
#         print(result)
#     else:
#         print('We have no {}!'.format(weapon_name))
# shop(weapon,quantity,money)