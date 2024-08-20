import sys
from collections import deque

# 입력 받기
N, K = map(int, input().split())

# 큐 초기화
queue = deque([ for i in range(1, N + 1))
print("<",end='')

# 큐에서 K번째 사람 제거 및 결과 리스트에 추가
while True:
    for _ in range(K-1):
        queue.append(queue.popleft())
    print(queue.popleft(),end='')
    if queue: 
        print(', ',end='') # 출력 형태 맞춰 출력하기
    else :
        break

# 결과 출력
print('>')
