def min_energy_to_meet(N, blocks):
    dp = [float('inf')] * N  # dp 배열 크기를 N으로 설정
    dp[0] = 0  # 첫 번째 블록 도달 비용은 0

    target_sequence = "BOJ"

    for i in range(N):
        if dp[i] == float('inf'):
            continue
        
        for j in range(i + 1, N):
            expected_char = target_sequence[(j - 1) % 3]
            if blocks[j] == expected_char:
                jump_distance = j - i
                dp[j] = min(dp[j], dp[i] + jump_distance * jump_distance)

    return dp[N - 1] if dp[N - 1] != float('inf') else -1  # 마지막 블록에 대한 결과

N = int(input())
blocks = input().strip()

print(min_energy_to_meet(N, blocks))
