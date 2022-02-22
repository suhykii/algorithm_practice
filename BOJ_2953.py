ls = []
for i in range(5):
    score = sum(map(int, input().split()))
    ls.append(score)

print(ls.pop(max(ls)), max(ls))