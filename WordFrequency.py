readfile = open("sometext.txt", "r")
dic = {}
for i in readfile:
    split = i.split()
for i in split:
    dic[i] = split.count(i)
print(dic)