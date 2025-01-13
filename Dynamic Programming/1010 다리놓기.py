'''
    1010번 "다리놓기" 실버 5
    
    DP
'''

import sys


T = int(sys.stdin.readline().strip())

for _ in range(T):  # 테스트 케이스만큼 반복
    N, M = map(int,sys.stdin.readline().strip().split())

    # dp의 초기값 설정
    dp = [ [0 for _ in range(M+1)] for _ in range(N+1)]
    for i in range(1,M+1):
        dp[1][i] = i
        
    for i in range(1,N+1):
        for j in range(M+1):
            # F(N,M) = F(N-1,M-1) + F(N-1,M-2) + … + F(N-1,N-1)
            # 작은수 N-1 ~ 큰수 M-1 까지
            for k in range(i-1,j): 
                # k => n-1 ~ m-1까지인 수
                # dp[i][j] = dp[i][j] + dp[i-1][k]
                dp[i][j] += dp[i-1][k]
    
    print(dp[N][M])
            