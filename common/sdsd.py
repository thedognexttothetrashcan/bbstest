import requests

for i in range(10):
    res = requests.get(url='http://127.0.0.1:8000/')
    print(res.text)

post = [(2, 4), (6, 23), (12, 56), (74, 25)]

print(sorted(post, key=lambda post: -post[1], reverse=True))
print(sorted(post, key=lambda post: -post[1]))

print(post.index((2, 4)))


def foo(x):
    print(sorted(x))


foo(post)

cleaned_data = [[1, 2], [3, 4], [5, 6]]
post = {
    1: 'aa',
    3: 'bb',
    5: 'cc'
}
for item in cleaned_data:
    post_id = item[0]
    # print(post_id)
    item[0] = post[post_id]
    print(item[0])
print(cleaned_data)
