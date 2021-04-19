# Вывести от 1 до 100
# i = 0
# while i <= 100:
#     print(i)
#     i += 1

# Вывести все четные из списка
# numbers = [1,2,3,4,5,6,7,8,9,0]
# i = 0
# while i < len(numbers):
#     if numbers[i] % 2 == 0:
#         print(numbers[i])
#     i += 1

# Сумма всех чисел списка
# numbers = [1,2,3,4,5,6,7,8,9,0]
# print(sum(numbers))

# Максимальноe число списка
# numbers = [1,2,3,4,5,6,7,8,9,0]
#
# max_number = 0
# i = 0
# while i < len(numbers):
#     if numbers[i] > max_number:
#         max_number = numbers[i]
#     i += 1
# print(max_number)



# Сумма всех чисел списка
# numbers = [1,2,3,4,5,6,7,8,9,0]
#
# i = 0
# summ = 0
#
# while i < len(numbers):
#     summ += numbers[i]
#
#     i += 1
# print(summ)

# Второй макксимум списка
# numbers = [1,2,3,4,5,6,7,8,9,0]
# i = 0
# max_num = 0
# while i < len(numbers):
#     if numbers[i] > max_num:
#         max_num = numbers[i]
#     i += 1
#
# second = 0
# i = 0
# while i < len(numbers):
#     if numbers[i] > second and numbers[i] < max_num:
#         second = numbers[i]
#     i += 1
# print(max_num, second)


# numbers = [1,1,2,3,4,5,6,6,10,25,17,18]
# i = 0
# gt_ten = 0
# while i < len(numbers):
#     if numbers[i] > 10:
#         gt_ten += 1
#     i += 1
# print(gt_ten)

# numbers = [1,1,2,3,4,7,15,66,5,6,6,10,25,17,18]
# i = 0
# uniq_numbers = []
# while i < len(numbers):
#     if numbers[i] not in uniq_numbers:
#         uniq_numbers.append(numbers[i])
#     i += 1
# uniq_numbers.sort()
# print(uniq_numbers)



# 1
# num = [1,1,2,3,4,7,15,66,5,6,6,10,25,17,18]
# num1 = []
# i = 0
# while i < 1:
#     num1.append(num[::2])
#     i += 1
# print(num1)



# 2
# num = [1,1,2,3,4,7,15,66,5,6,6,10,25,17,18]
#
# max_number = 0
# i = 0
# while i < len(num):
#     if num[i] > max_number:
#         max_number = num[i]
#     i += 1
# print(max_number)


# 3
# num = [1,1,2,3,4,7,15,66,5,6,6,10,25,17,18]
# num.reverse()
# print(num)

# 4
# num = [1,1,2,3,4,7,15,66,5,6,6,10,25,17,18]
# num1 = []
# max_number = 0
# i = 0
# while i < len(num):
#     if num[i] > max_number:
#         max_number = num[i]
#     i += 1
# print(max_number)
# print(num.index(max_number))


# 7
# num = [-1,1,2,3,4,-7,15,-66,-5,6,6,10,25,17,18]
# num1 = []
# i = 0
# while i < len(num):
#     if num[i] > 0:
#         num1.append(num[i])
#     i += 1
# print(len(num1))
# print(num1)

# 8
# num = [-1,1,2,-3,4,-7,15,-66,-5,6,-6,10,25,17,-18]
# num1 = []
# i = 0
# while i < len(num):
#     if num[i] < 0:
#         num1.append(num[i])
#     i += 1
# print(len(num1))
# print(num1)



# num = [1,1,2,3,4,7,15,66,5,6,6,10,25,17,18]
#
# k = 3
# c = 10
# num.insert(k,c)
# print(num)