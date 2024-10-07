#백준 1913번
import sys
input=sys.stdin.readline


#하-우-상-좌
# dr=[1,0,-1,0]
# dc=[0,1,0,-1]

#상-우-하-좌
dr=[-1,0,1,0]
dc=[0,1,0,-1]
targetR=0
targetC=0

N=int(input())
NUMBER=int(input())
ANSWER=[]
snail=[[0]* N for _ in range(N)] #2차원 리스트 초기화
# r=c=d=0
d=0
r=N//2
c=N//2

# N**N 부터 1까지 차례로 순회하며 할당한다.
for num in range(1,N**2+1):
    #해당 좌표에 해당 숫자를 할당한다.

    snail[r][c]=num

    #기본적으로 기존 방향을 유지하며 다음 좌표를 설정한다.
    nr=r+dr[d]
    nc=c+dc[d]

    #다음 좌표가 범위를 벗어나는 경우 또는 다음 좌표에 이미 숫자가 할당된 경우 방향을 전환한다.
    #단축 평가를 조심하자

    if nr<0 or nr>=N or nc<0 or nc>=N or snail[nr][nc] !=0:
        #아래와 같이 방향 전환 좌표를 설정하면 3=>0으로의 방향 전환이 가능하다.
        d=(d+1)%4
        nr = r + dr[d]
        nc = c + dc[d]

    #위에서 계산한 다음 좌표를 현재 좌표로 최신화 한 후 다음 반복으로 넘어간다.
    r=nr
    c=nc

for i,row in enumerate(snail):
    for j,value in enumerate(row):
        if value==NUMBER:
            ANSWER.append(i+1)
            ANSWER.append(j+1)
    print(*row)

print(*ANSWER)




