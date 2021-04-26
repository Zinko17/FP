import pprint
blogs = [{'id':1,'title':'MyFirstBlog','description':'lalal2'},
        {'id':2,'title':'Travel','description':'lalal2'},
        {'id':3,'title':'Food','description':'lalal2'},
        {'id':4,'title':'Music','description':'lalal2'},
        {'id':5,'title':'Movies','description':'lalal2'},
        {'id':6,'title':'Books','description':'lalal2'},
        ]
posts = [
    {'id':1,'blog_id':1,'subject':'learn python','text':'wooh','rate':9.8},
    {'id':2,'blog_id':1,'subject':'develop program','text':'wooh','rate':7},
    {'id':3,'blog_id':1,'subject':'learn framework','text':'wooh','rate':10},
    {'id':4,'blog_id':2,'subject':'mountain','text':'wooh','rate':3},
    {'id':5,'blog_id':3,'subject':'fast-food','text':'wooh','rate':8.9},
    {'id':6,'blog_id':4,'subject':'rock!','text':'wooh','rate':5.7},
    {'id':7,'blog_id':2,'subject':'lakes','text':'wooh','rate':1.2},
    {'id':8,'blog_id':3,'subject':'plov','text':'wooh','rate':7},
    {'id':9,'blog_id':6,'subject':'ABC','text':'wooh','rate':10},
    {'id':10,'blog_id':2,'subject':'woods','text':'wooh','rate':2.1},
    {'id':11,'blog_id':3,'subject':'pizza','text':'wooh','rate':4.2},
    {'id':12,'blog_id':4,'subject':'classic','text':'wooh','rate':6.6},
    {'id':13,'blog_id':5,'subject':'Lord of The Rings','text':'wooh','rate':10},
    {'id':14,'blog_id':5,'subject':'Wrath of Man','text':'wooh','rate':0.9},
]
for blog in blogs:
    rate_sum = 0
    post_q = 0
    for post in posts:
        if blog['id'] == post['blog_id']:
            rate_sum += post['rate']
            post_q += 1
            rate_avg = rate_sum/post_q
            round(rate_avg,1)
            blog['Average'] = rate_avg


for blog in blogs:
    top = 0
    if blog['Average'] > top:
        top += blog['Average']
# print(top,blog['id'])

for post in posts:
    top_p = 0
    if post['rate'] >= top_p:
        top_p += post['rate']
print(top_p)


