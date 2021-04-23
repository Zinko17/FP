# def sum_of_3 (a,b,c):
#     print(a+b+c)
# sum_of_3(1,2,3)



# def max_of_list(numbers):
#     return max(numbers)
# print(max_of_list([1,3,5,7,2]))
# print(max_of_list([1,3,5,7,211,24354,352352]))


def maximum_of_2():
    num1 = int(input())
    num2 = int(input())
    if num1 > num2:
        print(num1)
    else:
        print(num2)
# maximum_of_2()
# maximum_of_2()


# def register(username,password,confirm_password):
#     if password == confirm_password:
#         return username,password
#     else:
#         print('Пароли не совпадают')
#
# username,password = register('harryyy','123456', '123456')
# # print(username,password)
#
# def auth(username1,password1):
#     if username1 == username and password1 == password:
#         print('Вы вошли в систему!')
#     else:
#         print('Логин или пароль не совпадает!')
# auth('harry','123456')
# i = 0
# while i < 1:
#     def register(username, password,check_password):
#         if len(username) >= 8 and password == check_password and not password.isalpha():
#             return username,password
#
#     try:
#         username,password = register('harryyyy', '123456','123456')
#         print('Регистрация завершена!')
#     except TypeError:
#         print('Введите правильные данные!')
#         break
#     i += 1
#
# def auth():
#     for i in range(3):
#         username1 = input('Введите логин:')
#         password1 = input('Введите пароль:')
#         if username1 == username and password1 == password:
#             print('Вы вошли в систему!')
#             break
#         else:
#             print('Логин или пароль не совпадает!')
# auth()
#