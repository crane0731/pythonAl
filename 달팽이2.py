#백준 1913번
import sys

from unicodedata import numeric

input=sys.stdin.readline

#하-우-상-좌
dr=[1,0,-1,0]
dc=[0,1,0,-1]

N=int(input())
NUMBER=int(input())
ANSWER=[]
snail=[[0]* N for _ in range(N)] #2차원 리스트 초기화
d=0
r=-1
c=0
num = N**2  # 달팽이 안에 넣을 숫자

for i in range(N*2,1,-1): #방향 바꾸기 횟수 2n-1
    for _ in range(i//2): #각 방향에서 움직임 횟수
         r+=dr[d%4]
         c+=dc[d%4]
         snail[r][c]=num
         num -= 1
    d+=1 #방향 바꾸기

for i,row in enumerate(snail):
    for j,value in enumerate(row):
        if value==NUMBER:
            ANSWER.append(i+1)
            ANSWER.append(j+1)
    print(*row)

print(*ANSWER)
