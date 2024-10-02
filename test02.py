
#백준 2559번
#0번 인덱스 부터  K번째 까지의 구간 합을 구한다. ->first
#그 다음 부터 first의 값에서 시작 인덱스 보다 1인덱스 작은 값을 빼고 K번째의 값을 더한다/.
# 값들을 리스트에 넣는다.



import sys

input=sys.stdin.readline
N,K = map(int, input().split())
nums = list(map(int, input().split()))
temp=0
result=[]

temp=sum(nums[:K])
result.append(temp)

for i in range(1,N-K+1):
    temp=temp-nums[i-1]+nums[i+K-1]
    result.append(temp)

print(max(result))

