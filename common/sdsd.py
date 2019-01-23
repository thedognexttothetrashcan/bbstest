# import requests
#
# for i in range(10):
#     res = requests.get(url='http://127.0.0.1:8000/')
#     print(res.text)
#
# post = [(2, 4), (6, 23), (12, 56), (74, 25)]
#
# print(sorted(post, key=lambda post: -post[1], reverse=True))
# print(sorted(post, key=lambda post: -post[1]))
#
# print(post.index((2, 4)))
#
#
# def foo(x):
#     print(sorted(x))
#
#
# foo(post)
#
# cleaned_data = [[1, 2], [3, 4], [5, 6]]
# post = {
#     1: 'aa',
#     3: 'bb',
#     5: 'cc'
# }
# for item in cleaned_data:
#     post_id = item[0]
#     # print(post_id)
#     item[0] = post[post_id]
#     print(item[0])
# print(cleaned_data)
from random import sample, randint

l = [i for i in range(1,100)]
a = 1,2,3,4,5,6

date = [randint(10,20) for _ in range(10)]
c = sample(date, 5)
v = sample(l, 10)
aa = str(v).strip('[]').replace(',','')
a1 = eval('+'.join(aa))
# print(a1)
# while True:
a3 = []
for i in range(100):
    a = eval('+'.join(aa))
    if a not in range(100,132):
        # print(a)
        continue
    else:
        a3.append(a)
        break
print(a3)