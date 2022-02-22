F = "CAMBRIDGE"
W = input()
for i in F[:]:
    W = W.replace("{}".format(i), "")
print(W)