import sys
input = sys.stdin.readline

n,s,m = map(int,input().split())
v = list(map(int,input().split()))

#dp정의 
d=[[0]*(m+1) for _ in range(n+1)]
#처음 시작
d[0][s] =1

for i in range(1,n+1): #곡의 개수 만큼 
    for j in range(m+1):
        if d[i-1][j]!=0: #볼륨 조절 가능하면 
            if 0<=j+v[i-1]<=m:
                d[i][j+v[i-1]]=1
            if 0<=j-v[i-1]<=m:
                d[i][j-v[i-1]]=1
ans =-1
#볼륨의 최대값을 출력하기 위해 내림차순으로 반복문 실행 
for i in range(m, -1, -1):
    if d[n][i]==1: #최대값 발견하면 중단 
        ans = i
        break
    
print(ans)