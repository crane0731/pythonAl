import sys


input=sys.stdin.readline

N=int(input())

arr = [[0] * (N) for _ in range(N)]  # 이차원리스트 기본 틀

dr=[1,-1,0,0] #아무 방향이나 설정
dc=[0,0,-1,1]

answer=0 #max가 될 수 있는 값 설정

for i in range(N):
        arr[i]=list(map(int, input().split()))

def dfs(r,c):
    cnt=1;
    arr[r][c]=0;
    stack=[]
    stack.append([r,c]) #스택에 맨 처음 값 넣고 시작

    while stack:
        current=stack.pop()
        cur_r=current[0]
        cur_c=current[1]

        #4방을 탐색 하면서
        for i in range(4):
            nr=cur_r+dr[i]
            nc=cur_c+dc[i]
        

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            if arr[nr][nc]==0:
                continue

            stack.append([nr,nc])
            arr[nr][nc]=0 # 그 자리를 0으로 만듦
            cnt+=1 # 그리고 마을을 하나 찾았다고 기록

    return cnt

#행 우선 순회를 하면서 + 사람이 있는 집을 발견한경우?
for i in range(N):
    for j in range(N):
        if arr[i][j]==1:
            answer = max(answer, dfs(i,j))

print(answer) #마을 군집의 최대값 출력=>13