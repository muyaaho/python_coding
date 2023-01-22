n = int(input())
dp = [[0]*10 for i in range(n+1)]

for i in range(1,10):
    dp[1][i] = 1

for i in range(2, n+1):    # 1, 10, 100의 자리
    for j in range(10):  # 1의 자리 -> 세로로 생각
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[-1])%1000000000)