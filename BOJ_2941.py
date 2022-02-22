croat_ls = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()
for i in croat_ls:
    word = word.replace(i, "1")
print(len(word))

