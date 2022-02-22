T = int(input())
for i in range(T):
    num, word = input().split()
    num = int(num)
    ls = ""
    for i in range(len(word)):
        s = num*word[i]
        ls += s
    print(ls)