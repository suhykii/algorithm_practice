n = int(input())
li = []
for i in range(n):
    num = int(input())
    li.append(num)
li = sorted(li)
for i in range(n):
    print(li[i])