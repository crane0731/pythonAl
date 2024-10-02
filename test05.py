#백준 1543번
import sys
input=sys.stdin.readline

text = str(input()).rstrip()
answer = str(input()).rstrip()
count=0
index=0

for i in range(len(text)-len(answer)+1):

    print(text[index : len(answer) + index])
    print(answer)

    if text[index : len(answer)+index]==answer:
        count+=1
        index+=len(answer)
        print("index="+str(index))

        print("일치")
        print()
    else:
        index+=1
        print("불일치")
        print()

print(count)