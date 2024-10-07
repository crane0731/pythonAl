#프로그래머스 실습용 로봇 문제
def solution(command):
    x = y = d = 0 #초기 좌표와 방향

    dx = [0, 1, 0, -1] #상 우 하 좌
    dy = [1, 0, -1, 0]

    for move in command:
        if move=="R":
            d+=1
        elif move=="L":
            d-=1
        elif move=="G":
            x+= dx[d % 4]
            y+= dy[d % 4]
        elif move =="B":
            x-= dx[d % 4]
            y-= dy[d % 4]

    return[x,y]

result=solution("GRGRGRB")
print(result)




