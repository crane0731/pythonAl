# 이 문제의 input은 아래와 같이 입력됩니다. (단방향이면 문제가 알려줌)
# 7 8 # V(정점의 개수), E(간선의 개수)
# 1 2 # E줄에 걸쳐 간선 정보 입력
# 1 3
# 2 4
# 2 5
# 4 6
# 5 6
# 6 7
# 3 7

V,E = map(int,input().split())

adj_list=[[]for _ in range(V+1)]

for _ in range(E):
    start,end=map(int,input().split())
    adj_list[start].append(end)
    adj_list[end].append(start) #양방향

# adj_list = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
