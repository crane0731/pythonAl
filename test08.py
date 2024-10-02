arr=[[1,2,3],
     [4,5,6],
     [7,8,9]]
dr=[1,-1,0,0] #하, 상, 좌, 우
dc=[0,0,-1,1]
r=c=2

for i in range(4):
    nr=r+dr[i]
    nc=c+dc[i]

    if nr<0 or nr>=3 or nc<0 or nc>=3:
        continue

    print(arr[nr][nc])

