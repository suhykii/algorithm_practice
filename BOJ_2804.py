A, B = input().split()
idx1_ls =[]
for i in A:
    idx1=B.find(i)
    if idx1 < 0:
        pass
    else:
        idx1_ls.append(idx1)
idx2_ls =[]
for i in B:
    idx2=A.find(i)
    if idx2 < 0:
        pass
    else:
        idx2_ls.append(idx2)
ls = []
for i in range(len(B)):

    s = "."*len(A[:idx2_ls[0]])+B[i]+"."*len(A[idx2_ls[0]+1:])
    ls.append(s)
ls[idx1_ls[0]] = A
for i in ls:
    print(i)