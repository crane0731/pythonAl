#백준 2566번
import sys
input=sys.stdin.readline

temp=0
row=0
col=0
matrix = []
for _ in range(9):
    N = list(map(int, input().split()))  # 한 줄씩 입력받아 리스트로 변환
    matrix.append(N)

for i in range(9):
    for j in range(9):
        if matrix[i][j]>=temp:
            temp=matrix[i][j]
            row=i+1
            col =j+1

print(temp)
print(row, col)

