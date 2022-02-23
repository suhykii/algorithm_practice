li = [input().split()]
T = len(li) 
dic = {}
for i in range(T):
    cnt = 1
    if li[i] in dic.keys():
        cnt +=1
        dic["li[i]"] = cnt
    else:
        dic["li[i]"] = cnt

print(dic)