def solution(maps):
    N = len(maps)
    M = len(maps[0])

    Q = []
    dist = [M * [0] for _ in range(N)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]
    flag = False

    Q.append([0, 0])
    dist[0][0] = 1

    while (Q):
        current = Q.pop(0)
        cur_r = current[0]
        cur_c = current[1]

        if cur_r == N - 1 and cur_c == M - 1:  # 해당 위치를 찾은 경우
            flag = True  # 찾았다고 체크
            break

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if maps[nr][nc] == 0 or dist[nr][nc] > 0:
                continue

            dist[nr][nc] = dist[cur_r][cur_c] + 1
            Q.append([nr, nc])

    return dist[N - 1][M - 1] if flag else -1


def main():
    # 여기에 메인 함수의 로직을 작성
    result = solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]])
    print(result)


if __name__ == "__main__":
    main()
