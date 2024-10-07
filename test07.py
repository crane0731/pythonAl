
# direction: 0=위, 1=왼쪽, 2=아래, 3=오른쪽
direction = 2
x = 0
y = 0


def go():
    global x, y, direction
    print("go")
    if direction == 0:
        y -= 1
    elif direction == 1:
        x -= 1
    elif direction == 2:
        y += 1
    elif direction == 3:
        x += 1
    print(x, y)


def back():
    global x, y, direction
    print("back")
    if direction == 0:
        y += 1
    elif direction == 1:
        x += 1
    elif direction == 2:
        y -= 1
    elif direction == 3:
        x -= 1
    print(x, y)


def turnRight():
    global direction
    print("turnRight")
    direction = (direction + 1) % 4


def turnLeft():
    global direction
    print("turnLeft")
    direction = (direction - 1) % 4


def solution(command):
    global x, y
    print("초기 위치", x, y)
    for i in command:
        if i == 'R':
            turnRight()
        elif i == 'L':
            turnLeft()
        elif i == 'G':
            go()
        elif i == 'B':
            back()
    print("최종 위치", x, y)


# 명령어 실행
solution("GRGLGRG")
solution("GRGRGRB")