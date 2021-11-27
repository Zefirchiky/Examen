dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for i,t in dic.items():
    if t%2==0:
        dic[i] = "even"
    else:
        dic[i] = "odd"
print(dic)
