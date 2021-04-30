customers = [
    {'id': 1, 'username': 'steeve', 'age': 22, },
    {'id': 2, 'username': 'Gena', 'age': 22, },
    {'id': 3, 'username': 'santino', 'age': 22, },
    {'id': 4, 'username': 'francisco', 'age': 22, },
    {'id': 5, 'username': 'dagny', 'age': 22, },
    {'id': 6, 'username': 'johngalt', 'age': 22, },
]
annotate = {
    'M': '000000',
    'K': '000',
    'H': '00',
    'B': '000000000'
}
purchases = [
    {'id': 1, 'user_id': 2, 'product_name': 'tesla obligations', 'total_amount': '40M'},
    {'id': 2, 'user_id': 3, 'product_name': 'cigarettes', 'total_amount': '120K'},
    {'id': 3, 'user_id': 1, 'product_name': 'beer', 'total_amount': '9H'},
    {'id': 4, 'user_id': 4, 'product_name': 'cake', 'total_amount': '400K'},
    {'id': 5, 'user_id': 6, 'product_name': 'chair', 'total_amount': '4M'},
    {'id': 6, 'user_id': 5, 'product_name': 'coca-cola obligations', 'total_amount': '20B'},
]
"""
1. Соединить два словаря customers и purchases в новый словарь.
    1.1 Удалить из purchases ключ - id
    1.2 После слияния словарей - удалить ключ - user_id
2. Ключ total_amount в результативном списке - перевести в целое число, используя аннотацию
"""

import pprint


def task1():
    for purchase in purchases:
        purchase.pop('id')


    for customer in customers:
        for purchase in purchases:
            if customer['id'] == purchase['user_id']:
                customer.update(purchase)

    for customer in customers:
        customer.pop('user_id')

    return customers
task1()
# pprint.pprint(customers)


def task2():
    for customer in customers:
        for ann in annotate:
            customer['total_amount'] = (customer['total_amount'].replace(ann,annotate[ann]))
        customer['total_amount'] = int(customer['total_amount'])

    return customers


task2()
pprint.pprint(customers)