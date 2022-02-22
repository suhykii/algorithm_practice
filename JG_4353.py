arr1_name = input()
arr1 = [list(map(int, input().split())) for _ in range(2)]
arr2_name = input()
arr2 = [list(map(int, input().split())) for _ in range(2)]
answer = [arr1[i][j]*arr2[i][j] for i in range(2) for j in range(8)]
print(answer)