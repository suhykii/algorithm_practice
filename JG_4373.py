T = int(input())
dic = {}
for _ in range(T):
    a , b = input().split()
    dic[f"{a}"] = f"{b}"

print(dic.get(input(), "Unknown Country"))