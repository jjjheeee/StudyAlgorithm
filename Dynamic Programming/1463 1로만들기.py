'''
    1463번 "1로 만들기" 실버 3
    
    DP
    
    문제
        정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

        X가 3으로 나누어 떨어지면, 3으로 나눈다.
        X가 2로 나누어 떨어지면, 2로 나눈다.
        1을 뺀다.
        정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

    입력
        첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

    출력
        첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
'''
import sys

N = int(sys.stdin.readline().strip())

INF = int(10e9) # 최소값 비교를 위한 최대값 설정
dp = [INF for _ in range(1000001)] # 최대값으로 dp 설정

# dp의 최소 단위 설정
dp[1] = 0
dp[2] = 1
dp[3] = 1

# dp의 값 채우기
for i in range(4,N+1):
    
    min_count = INF
    
    if i % 3 == 0:
        min_count = min(min_count, dp[i//3])
    
    if i % 2 == 0:
        min_count = min(min_count, dp[i//2])
        
    min_count = min(min_count, dp[i-1])
    
    dp[i] = min_count + 1
    
print(dp[N])