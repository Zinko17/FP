# """
# 1.Всем работникам месяца увеличить зарплату на 10%
# 2.Отделу где больше одного работников месяца увеличить зарплату на 5% дополнительно
# 3.Отдел где нет работников месяца - уменьшить всем зарплату на 3%
# 4.Работники чьи email-не принадлежат гуглу все кроме [@google.com,@gmail.com] - уволить
# """
# import pprint
# data = [
#     {'user': 'digital', 'email': 'digital@google.com', 'age': 23, 'salary': 200000, 'department': 'IT'},
#     {'user': 'sam', 'email': 'digital', 'age': 23, 'salary': 200000, 'department': 'manager'},
#     {'user': 'john', 'email': 'john@google.com', 'age': 23, 'salary': 200000, 'department': 'CEO'},
#     {'user': 'sparrow', 'email': 'digital@go.com', 'age': 23, 'salary': 200000, 'department': 'SEO'},
#     {'user': 'orlando', 'email': 'digital@gmail.com', 'age': 23, 'salary': 200000, 'department': 'food'},
#     {'user': 'ben', 'email': 'digi', 'age': 23, 'salary': 200000, 'department': 'worker'},
#     {'user': 'stiller', 'email': 'digital@apple.com', 'age': 23, 'salary': 200000, 'department': 'loan'},
#     {'user': 'adam', 'email': 'email@gmail.com', 'age': 23, 'salary': 200000, 'department': 'credit'},
#     {'user': 'eva', 'email': 'digital@google.com', 'age': 23, 'salary': 200000, 'department': 'buying'},
#     {'user': 'frodo', 'email': 'digital@google.com', 'age': 23, 'salary': 200000, 'department': 'IT'},
#     {'user': 'harry', 'email': 'digital@google.com', 'age': 23, 'salary': 200000, 'department': 'IT'},
#     {'user': 'ron', 'email': 'digital@google.com', 'age': 23, 'salary': 200000, 'department': 'IT'},
#     {'user': 'germiona', 'email': 'digit', 'age': 23, 'salary': 200000, 'department': 'IT'},
#     {'user': 'gannibal', 'email': 'digital@google.com', 'age': 23, 'salary': 200000, 'department': 'food'},
#     {'user': 'lector', 'email': 'digital@google.com', 'age': 23, 'salary': 200000, 'department': 'food'}
# ]
# worker_of_month = {'IT': ['sparrow', 'ben', 'frodo', 'gannibal'],
#                    'credit': [],
#                    'loan': ['stiller'],
#                    'food': ['gannibal', 'lector']}
#
# same1 = []
# def remove_same(worker_of_month):
#     for key,name in worker_of_month.items():
#         same1.extend(name)
#     for same in name:
#         quantity = same1.count(same)
#         if quantity > 1:
#             name.remove(same)
#
#
#     return worker_of_month
#
# worker_of_month = remove_same(worker_of_month)
# # pprint.pprint(worker_of_month)
#
#
# def wom_increase(data,worker_of_month):
#     for worker_key,worker_value in worker_of_month.items():
#         for worker in worker_value:
#             for user in data:
#                 if user['user'] == worker:
#                     user['salary'] = user['salary'] + (user['salary'] * 0.1)
#     return data
#
# data = wom_increase(data,worker_of_month)
#
#
# def best_departments(data,worker_of_month):
#     for worker_key,worker_value in worker_of_month.items():
#             for worker in worker_value:
#                 for user in data:
#                     if len(worker_value) > 1:
#                         if user['user'] == worker:
#                             user['salary'] = user['salary'] + (user['salary'] * 0.05)
#
#     return data
#
# data = best_departments(data,worker_of_month)
# # pprint.pprint(data)
#
#
#
# def worst_departments(data,worker_of_month):
#     for user in data:
#         for worker in worker_of_month:
#             if len(worker_of_month[worker]) < 1 and user['department'] in worker:
#                 user['salary'] = user['salary'] - (user['salary'] * 0.03)
#
#     return data
#
# data = worst_departments(data,worker_of_month)
# # pprint.pprint(data)
#
# def remove_worker(data=data):
#     data_copy = data.copy()
#     for user in data_copy:
#         email = user['email']
#         if '@google.com' in email or '@gmail.com' in email:
#             pass
#         else:
#             data.remove(user)
#     return data
# data = remove_worker(data=data)
# pprint.pprint(data)