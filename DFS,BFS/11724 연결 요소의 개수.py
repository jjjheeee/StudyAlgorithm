'''
    11724번 "연결 요소의 개수" 실버 2
    
    그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
    
    문제
        방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

    입력
        첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. 
        (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N*(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. 
        (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

    출력
        첫째 줄에 연결 요소의 개수를 출력한다.
'''
import sys
sys.setrecursionlimit(10**6) # 파이썬은 재귀함수 깊이에 대한 제한이 있어 제한을 풀어줘야한다.

N, M = map(int, sys.stdin.readline().strip().split())

cycle_list = [False for _ in range(N+1)] 

# 연결 구조를 확인하는 함수
def check_cycle(node):
	cycle_list[node] = True
	for i in list_[node]:
		if not cycle_list[i] :
			check_cycle(i)

list_ = [[] for i in range(N+1)] # 2차원 리스트 초기화
# 값넣기
for i in range(M):
	u, v = map(int, sys.stdin.readline().strip().split())
	# 순열과는 다르게 순서가 없기 때문에 양방향 다 기록해준다.
	list_[u].append(v)
	list_[v].append(u)


# 정점의 갯수만큼 계산하기(정점은 1부터 시작)
cnt = 0
for i in range(1,N+1):
	if not cycle_list[i]:
		cnt += 1
		check_cycle(i)
print(cnt)