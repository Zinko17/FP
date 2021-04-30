# """"
# Соединение словарей
# """
#
# products1 = {'potato': 2, 'tomato': 3, 'pineapple': 4}
# products2 = {'apple': 50, 'onion':41, 'carrot': 30}
#
# products1.update(products2)
#
# print(products1)



import pprint

"""
1. Нужно найти все posts со статусом sponsored!
2. Найти комментарии к posts sponsored
3. Среди найденных комментариев найти те что содержат keyword из posts
"""

users = [{'id':1,'user': 'digital', },
         {'id':2,'user': 'maksim', },
         {'id':3,'user': 'vova', },
         {'id':4,'user': 'begimai', },
         {'id':5,'user': 'aliya', },
         {'id':6,'user': 'bakyt',},
         {'id':7,'user': 'chingiz', },
         {'id':8,'user': 'jamilya',},
         {'id':9,'user': 'cholpon', },
         {'id':10,'user': 'erbol', }
         ]

posts = [{'id':1,'text':'hiring','status':'sponsored','keyword':'nic1'},
         {'id':2,'text':'text1','status':'pub'},
         {'id':3,'text':'text2','status':'pub'},
         {'id':4,'text':'text3','status':'pub'},
         {'id':5,'text':'text4','status':'pub'},
         {'id':6,'text':'text5','status':'pub'},
         {'id':7,'text':'Canada immigration','status':'sponsored','keyword':'interested!'}]


comments = [{'id':1,'user_id':1,'post_id':1,'comment':'This is not nic1'},
            {'id':2,'user_id':2,'post_id':1,'comment':'Hello this is nic1'},
            {'id':3,'user_id':3,'post_id':2,'comment':'looking good!'},
            {'id':4,'user_id':4,'post_id':2,'comment':'awesome!'},
            {'id':5,'user_id':5,'post_id':2,'comment':'LGTM'},
            {'id':6,'user_id':6,'post_id':3,'comment':'here we go!'},
            {'id':7,'user_id':6,'post_id':4,'comment':'not ok'},
            {'id':8,'user_id':6,'post_id':7,'comment':'interested!'},
            {'id':9,'user_id':6,'post_id':7,'comment':'woohoo!'},
            {'id':10,'user_id':6,'post_id':7,'comment':'interested!'}]

def post_search(posts):
    posts1 = []
    """
    Функция поиска постов со статусом sponsored
    :param posts: Список со словарями, в которых данные публикаций
    :return: Список posts, с добавленными в него постами со статусами sponsored
    """
    for post in posts:
        if post['status'] == 'sponsored':
            posts1.append(post)

    return posts1

posts = post_search(posts)


def comments_search(posts,comments):
    """

    :param posts1:Список со словарями, в которых данные публикаций
    :param comments:Список со словарями, в которых данные комментариев
    :return:Измененные список posts, с комментариями к постам с статусом sponsored
    """
    for post in posts:
        post['comms'] = []
        for comment in comments:
            if comment['post_id'] == post['id']:
                post['comms'].append(comment['comment'])
    return posts

posts = comments_search(posts,comments)
# pprint.pprint(posts)


def keyword_search(posts):
    for post in posts:
        for comment in post['comms']:
            if post['keyword'] not in comment:
                post['comms'].remove(comment)
    return posts
posts = keyword_search(posts)
# pprint.pprint(posts)


def user_search(posts, comments, users,):
    users1 = []
    for user in users:
        for post in posts:
            for post_c in post['comms']:
                for comment in comments:
                    if post_c == comment['comment'] and user['id'] == comment['user_id']:
                        users1.append(user)

    return users1


users = user_search(posts,comments,users)
pprint.pprint(users,)