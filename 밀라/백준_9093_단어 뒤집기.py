t = int(input())
sentence = [list(map(str, input().split())) for _ in range(t)]

for i in range(t):
		resentence = []
		for j in range(len(sentence[i])):
				resentence.append(sentence[i][j][::-1])
		print(resentence)