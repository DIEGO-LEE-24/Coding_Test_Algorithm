# 리스트
# push append
# pop pop
# size len
# empty if stack:
# top stack[-1]
import sys
input = sys.stdin.readline

stack = []
n = int(input())

for _ in range(n):
    qry = input().strip().split()
    if qry[0] == 'push':
        stack.append(qry[1])
    elif qry[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif qry[0] == 'size':
        print(len(stack))
    elif qry[0] == 'empty':
        print(0 if stack else 1)
    elif qry[0] == 'top':
        print(stack[-1] if stack else -1)
        
