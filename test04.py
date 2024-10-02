#백준 10988
import sys
input=sys.stdin.readline

text = str(input()).rstrip()

indexL=0
indexR=-1
result=1
for i in range(len(text)//2):
    if text[indexL]==text[indexR]:
        indexL+=1
        indexR-=1
    else:
        result=0
        break

print(result)

