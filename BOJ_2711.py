T=  int(input())
for mis in range(T):
    num, wrong = input().split()
    a = int(num)
    print(wrong[:a-1]+wrong[a:])
