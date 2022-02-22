T = int(input())
for i in range(1, 1+T):
    if i%2 != 0:
        print(T*"* ")
    else:
        print(T*" *")