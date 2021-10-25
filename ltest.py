'''div = ['a', 'd']
dis1 = ["b", "c"]
dis2 = ["e", "f"]
dis = [dis1, dis2]

c = 0
for x in div:
    print(x)
    for i in dis[c]:
        for j in i:
            print(j)
    c += 1'''

a = 'localhost:8000/'
b = a.replace('/', '')
print(b)