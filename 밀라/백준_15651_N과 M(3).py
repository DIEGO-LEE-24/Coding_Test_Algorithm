import sys
input = sys.stdin.readline

def dfs(n, lst):
    if n == M:  
        answer.append(lst)
        return
    
    for i in range(1, N + 1):
        dfs(n + 1, lst + [i])

N, M = map(int, input().split())
answer = []

dfs(0, [])

for lst in answer:
    print(*lst)