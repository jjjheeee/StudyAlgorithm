'''
    5567번 "결혼식" 실버 2
    
    문제
        상근이는 자신의 결혼식에 학교 동기 중 자신의 친구와 친구의 친구를 초대하기로 했다. 
        상근이의 동기는 모두 N명이고, 이 학생들의 학번은 모두 1부터 N까지이다. 상근이의 학번은 1이다.

        상근이는 동기들의 친구 관계를 모두 조사한 리스트를 가지고 있다. 
        이 리스트를 바탕으로 결혼식에 초대할 사람의 수를 구하는 프로그램을 작성하시오.

    입력
        첫째 줄에 상근이의 동기의 수 n (2 ≤ n ≤ 500)이 주어진다. 
        둘째 줄에는 리스트의 길이 m (1 ≤ m ≤ 10000)이 주어진다. 
        다음 줄부터 m개 줄에는 친구 관계 ai bi가 주어진다. 
        (1 ≤ ai < bi ≤ n) ai와 bi가 친구라는 뜻이며, bi와 ai도 친구관계이다. 

    출력
        첫째 줄에 상근이의 결혼식에 초대하는 동기의 수를 출력한다.
'''

import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

# n+1 => n=6일때 친구는 1~6까지이지만 리스트는 0~5까지 나오기 떄문에 index 에러가 난다.
list_ = [[] for _ in range(n+1)] 
for _ in range(m):
	a,b = map(int, sys.stdin.readline().strip().split())
	list_[a].append(b)
	list_[b].append(a)

# 0이면 방문하지 않음
save_list = [0 for i in range(n+1)]

def bfs(start):
    index_list = [start] # 탐색의 시작 정점
    
    # 탐색할 정점이 존재하지 않을 경우 종료
    while index_list:
        index = index_list.pop(0)
        for i in list_[index]: # index 정점과 연결된 정점들
            if save_list[i] == 0: # 방문이력이 없다면 거리를 +1 하고 탐색할 정점으로 추가
                save_list[i] = save_list[index] + 1 # 시작부터 i까지의 거리, save_list[index] = 시작부터 i전까지의 거리
                index_list.append(i)
                
bfs(1) # 1부터 시작
count = 0

# 방문 탐색 거리를 저장한 리스트를 이용해 거리가 1이나 2인 수를 count 한다.
# 1은 본인이기 때문에 2부터 시작한다.
for i in range(2,n+1):
	if 1 <= save_list[i] <= 2:
		count += 1
print(count)


''' deque의 사용 '''
# import sys
# from collections import deque

# # 1. 문제의 input을 인접 그래프 형태로 받습니다.
# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)

# # 2. BFS 탐색헤 활용할 방문 배열을 선언합니다.
# visited = [0 for _ in range (n+1)]

# # 3. BFS 탐색을 구현합니다.
# def bfs(start):
#     que = deque([start]) # 3-1. queue를 만들고, 시작 정점을 추가합니다.

#     while que:
#         now = que.popleft() # 3-2. queue의 가장 앞 원소를 탐색합니다.
#         for x in graph[now]: # 3-3. 해당 정점과 연결된 정점들을 탐색합니다.
#             if visited[x] == 0: # 3-4. 방문된 정점이 아니라면, 방문표기(거리+1)을 하고 queue에 추가합니다.
#                 que.append(x)
#                 visited[x] = visited[now] + 1


# bfs(1)
# ans = 0
# # 4. BFS 탐색을 통해 구한 거리를 기반으로 정답을 구합니다.
# for i in range(2, n+1):
#     if 0 < visited[i] < 3:
#         ans += 1
# print(ans)