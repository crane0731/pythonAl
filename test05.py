#백준 1543번
import sys
input=sys.stdin.readline

text = str(input()).rstrip()
answer = str(input()).rstrip()
count=0
index=0

for i in range(len(text)-len(answer)+1):

    if text[index : len(answer)+index]==answer:
        count+=1
        index+=len(answer)
    else:
        index+=1

print(count)