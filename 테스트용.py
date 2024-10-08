import sys
input = sys.stdin.read

# 전역 변수 설정
N = 0
arr = []
dr = [1, -1, 0, 0]  # 상하좌우 이동을 위한 리스트
dc = [0, 0, -1, 1]
answer = 0

def dfs(r, c):
    cnt = 1
    arr[r][c] = 0  # 방문한 곳은 0으로 만듦
    stack = [(r, c)]  # 스택을 리스트로 생성하여 시작 좌표 넣기

    while stack:
        cur_r, cur_c = stack.pop()  # 스택에서 좌표 꺼내기

        # 4방향 탐색
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            # 범위 체크
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            # 이미 방문했거나 집이 없으면 넘어가기
            if arr[nr][nc] == 0:
                continue

            stack.append((nr, nc))  # 스택에 새 좌표 추가
            arr[nr][nc] = 0  # 방문한 곳은 0으로
            cnt += 1  # 마을 개수 추가

    return cnt

def main():
    global N, arr, answer

    # 입력 처리
    N = int(input().strip())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 행 우선 순회를 하며 dfs로 군집 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:  # 사람이 있는 집을 찾으면 dfs 시작
                answer = max(answer, dfs(i, j))

    print(answer)  # 마을 군집의 최댓값 출력

# 프로그램 시작
if __name__ == "__main__":
    main()
