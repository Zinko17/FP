# students = [{"name": "Vova",
#              "last_name": "Zinkovsky",
#              "age": 17,
#              "scores": [1, 2, 3, 4, 5],
#              "hobbies": ['play', 'programming', 'reading']
#              },
#             {"name": "Begimai",
#              "last_name": "Zhumakova",
#              "age": 18,
#              "scores": [5, 5, 3, 4, 5],
#              "hobbies": ['pubg', 'programming', 'reading', 'walking']
#              },
#             {"name": "Aliya",
#              "last_name": "Andabekova",
#              "age": 18,
#              "scores": [1, 4, 3, 1, 2],
#              "hobbies": ['programming', 'reading', 'drawing']
#              },
#             {"name": "Cholpon",
#              "last_name": "Kaimova",
#              "age": 16,
#              "scores": [5, 2, 4, 4, 5],
#              "hobbies": ['pubg', 'programming', 'reading', 'anime', ]
#              },
#             {"name": "Bakyt",
#              "last_name": "Asanaliev",
#              "age": 35,
#              "scores": [4, 2, 4, 4, 5],
#              "hobbies": ['play', 'programming', 'reading', 'footbal', 'history']
#              },
#             {"name": "Maksim",
#              "last_name": "Surovkin",
#              "age": 22,
#              "scores": [],
#              "hobbies": ['programming', 'reading', 'traveling', 'cycling']
#              }
#             ]
# general_avg = 0
# student_avg = []
# std = 0
# for student in students:
#     sum = 0
#     for score in student['scores']:
#         sum += score
#         try:
#             students_avg = sum / len(student['scores'])
#         except ZeroDivisionError:
#             students_avg = 0
#     student_avg.append(students_avg)
# sum_avg = 0
# for avg in student_avg:
#     sum_avg += avg
#     general_avg = sum_avg / len(student_avg)
# max = 0
# min = 5
# i = 0
#
# while i < len(student_avg):
#     if student_avg[i] > max:
#         max = student_avg[i]
#     elif student_avg[i] < min:
#         min = student_avg[i]
#     i += 1
# std = max - min
# print("student average:", student_avg)
# print("general average:", round(general_avg, 2))
# print("std:", round(std, 2))
#
# dict_loop = 0
#
# import pprint
#
# for student in students:
#     student['avg'] = student_avg[dict_loop]
#     dict_loop += 1
# pprint.pprint(students)



# import pprint
# data = [
#     {"dress":[
#                 {'name':'louis vuitton',
#                 'popularity':500,
#                  "price":1000
#                 },
#                 {'name':'versace',
#                 'popularity':210,
#                  "price":888
#                 },
#                 {'name':'supreme',
#                 'popularity':57,
#                  "price":765
#                 },
#     ]
#     },
#     {'jeans':[
#                 {'name':'adidas',
#                 'popularity':42,
#                  'price':2300
#                 },
#                 {'name':'armani',
#                 'popularity':678,
#                  'price':110
#                 },
#                 {'name':'casio',
#                 'popularity':230,
#                  'price':3000
#                 },
#     ]
#     },
#     {'t-shirt':[
#                 {'name':'tom ford',
#                 'popularity':999,
#                  'price':5000
#                 },
#                 {'name':'lacoste',
#                 'popularity':777,
#                  'price':230
#                 },
#                 {'name':'luxury',
#                 'popularity':876,
#                  'price':2300
#                 },
#     ]
#     }
# ]
# list1 = ['dress', 'jeans', 't-shirt']
#
# i = 0
# category_price = {}
#
# for category in data:
#     category_sum = 0
#     key = list1[i]
#     category_value = category[key]
#     for product in category_value:
#         category_sum += product['price']
#     category_price[key] = category_sum
#     i += 1
# print(max(category_price.values()))
#
# list2 = ['dress', 'jeans', 't-shirt']
# k = 0
# category_price2 = {}
# for category2 in data:
#     category_sum2 = 0
#     key2 = list1[k]
#     category_value2 = category2[key2]
#     for product2 in category_value2:
#         category_sum2 += product2['popularity']
#     category_price2[key2] = category_sum2
#     k += 1
# print(max(category_price2.values()))
#
#
# list3 = ['dress', 'jeans', 't-shirt']
# j = 0
# prices = []
#
# for max_price in data:
#     key3 = list3[j]
#     maxp_value = max_price[key3]
#     for product in maxp_value:
#         prices.append(product['price'])
#     j += 1
# print(max(prices),min(prices))





