# Неизменяемый список
# my_list = [1,2,3,4,5]
# my_tuple = (1,2,3,4,5)
# my_tuple.count()
# print(my_tuple)


# criminals = ['johny', 'sparrow', 'harry', 'jack', 'selena']
#
# name = input("Enter the name:")
# if name not in criminals:
#     criminals.append(name)
# print(criminals)

# import random
# i = 0
# user_info = [[],[]]
# while i < 1:
#     username = input("Enter the username:")
#     password = input ("Enter the password:")
#       check_password = input("Confirm your password:")
#     if password == check_password:
#         print("Data is correct")
#     else:
#         print("Password missmatch!")
#         break
#     code = random.randint(1000, 9999)
#     print("secret_code:", code)
#     check_code = int(input("Enter secret_code:"))
#     if code == check_code:
#         user_info[0].append(username)
#         user_info[1].append(password)
#     else:
#         print("Codes dont match!")
#         break
#     i += 1
#     username1 = input("Enter the username1:")
#     password1 = input("Enter the password1:")
#     if username1 in user_info[0] and password1 in user_info[1]:
#         print("Autorization complete!")
#     else:
#         print("Autorization failed!")
# print(user_info)

# import random
# user_info = [[],[]]
#
# count = 0
# username = input("Enter the username:")
# password = input ("Enter the password:")
# check_password = input("Confirm your password:")
# code = random.randint(1000, 9999)
# print("secret_code:", code)
# check_code = int(input("Enter secret_code:"))
#
# if len(username) >= 8 and len(password) >= 6:
#     if password == check_password:
#         print("Data is correct")
#         if code == check_code:
#             user_info[0].append(username)
#             user_info[1].append(password)
#         else:
#             print("Codes dont match!")
#     else:
#         print("Password missmatch!")
#
# print(user_info)
# print("please log in")
# tries = 0
# stop = None
# while tries < 3:
#     count = 0
#     username = input("Enter the username1:")
#     password = input("Enter the password1:")
#     while count < len(user_info):
#         print(count)
#         if username == user_info[0][count] and password == user_info[1][count]:
#             print("Autorization complete!")
#             stop = 'stop'
#             break
#         else:
#             print("Autorization failed!")
#         count += 1
#     if stop == 'stop':
#         break
#     tries += 1


