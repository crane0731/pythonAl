def solution(n, m, hole):

    maps=[n*[0]for _ in range(m)]
    dist = [m * [0] for _ in range(n)]

    for i in hole:
        maps[i[0]][i[1]]=1
    print(*maps)

    Q=[]
    dr=[1,-1,0,0]
    dc=[0,0,-1,1]
    flag = False

    Q.append([0,0])
    dist[0][0]=1





    return


def main():
    # 여기에 메인 함수의 로직을 작성
    result=solution(4,4,[[2, 3], [3, 3]])

if __name__ == "__main__":
    main()