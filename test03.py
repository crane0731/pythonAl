#백준11659번
#수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.
import sys

input=sys.stdin.readline

N,M = map(int, input().split())
nums = list(map(int, input().split()))

result=[]
for i in range(1,len(nums)):
    nums[i]+=nums[i-1]

for index in range(M):
    i,j=map(int,input().split())
    if i-2>=0:
        result.append(nums[j-1]-nums[i-2])
    else:
        result.append(nums[j-1])

for i in result:
    print(i)
## i부터 j까지의 구간합은 j까지의 구간합 - i까지의 구간합

