"""Взаимодействие с индексом и элементом одновременно"""

# list1 = ['red','blue', 'white']
# dict1 = {'name': "aliya"}
# for i, color in enumerate(list1):
#     print(i, color)
#
# for key,value in dict1.items():
#     print(key,value)
"""zip"""
# iterat = zip(*dict1)
# print(iterat)


# file1 = open('text.txt', 'w')
# file1.write('hello')


# data = [
#     {'text':'oh hi duuuude how r uy??check this 1xbet'},
#     {'text':'Dear Harry Potter, i am Frodo Baggins 1xbet represent 1xbet company.Best bet service'},
#     {'text':'wooooh yoow harry look at my jackpot 100000000$ at 1xbet service'},
#     {'text':'Harry , today i saw the man who looks like Hawkeye from Avengers on 100% and he dont use 1xbet service'},
# ]

# spam_word = ''
# qspam_word = 0
# for i in data:
#     data1 = i['text'].split()
#     print(data1)
#     for word in data1:
#         quantity = data1.count(word)
#         if quantity > qspam_word:
#             qspam_word = quantity
#             spam_word = word
# print(spam_word)
# final_mail = 'Hello Harry, my name is Maksim, Im  still waiting for the letter from Hogwarts'
# if spam_word in final_mail:
#     print('Final_mail is spam!!!')
# else:
#     print('Final_mail is not spam')

# q_spam = 0
# database = []
# spam_word = ''
# for mail in data:
#     str = mail['text'].lower().split()
#     database.extend(str)
#
# for word in database:
#     quantity = database.count(word)
#     print(quantity)
#     if quantity > q_spam:
#         q_spam = quantity
#         spam_word = word
# print(q_spam, spam_word)
#
# final_mail = 'Hello Harry, my name is Maksim, Im  still waiting for the letter from Hogwarts'
#
# if spam_word in final_mail.lower():
#     print('Final_mail is spam!!!')
# else:
#     print('Final_mail is not spam')



