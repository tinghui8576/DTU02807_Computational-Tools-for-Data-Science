from functools import reduce

text = 'Deer Bear River Car Car Bear Deer Car River Bear'


words = text.split()
# wfreq=[words.count(w) for w in words]
# print(dict(zip(words,wfreq)))

l = sorted(list(map(lambda x: (x, 1), words)))

print(l)
def func(w,t):
    print(w,t)
ans = reduce(func, l)
print(ans)