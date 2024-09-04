result = {}
team = ['A', 'B', 'C', 'D', 'E', 'F']
allMatch = []

for i in range(6):
    for j in range(i + 1, 6):
        allMatch.append([team[i], team[j]])

position = {'A': 0, 'B': 3, 'C': 6, 'D': 9, 'E': 12, 'F': 15}

def match(depth, note):
    if depth == 15:  
        result[str(note)] = True
        return

    for i in range(len(note)):
        if note[i] > answer[i]:  
            return

    a, b = allMatch[depth]
    aIDX = position[a]
    bIDX = position[b]

    note_win = note[:]
    note_win[aIDX] += 1
    note_win[bIDX + 2] += 1
    match(depth + 1, note_win[:])

    note_draw = note[:]
    note_draw[aIDX + 1] += 1
    note_draw[bIDX + 1] += 1
    match(depth + 1, note_draw[:])

    note_lose = note[:]
    note_lose[aIDX + 2] += 1
    note_lose[bIDX] += 1
    match(depth + 1, note_lose[:])

for _ in range(4):
    answer = list(map(int, input().split()))  
    match(0, [0] * 18)  

    if str(answer) in result:  
        print(1, end=' ')
    else:
        print(0, end= ' ')
