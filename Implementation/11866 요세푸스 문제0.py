'''
    11866번 "요세푸스 문제 0" 실버 4
    
    구현, 자료 구조, 큐
    
    문제
        요세푸스 문제는 다음과 같다.

        1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 
        이제 순서대로 K번째 사람을 제거한다. 
        한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 
        이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 
        예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

        N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

    입력
        첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 1,000)

    출력
        예제와 같이 요세푸스 순열을 출력한다.
'''

import sys
from collections import deque

N, K = map(int,sys.stdin.readline().strip().split())

result_list = []

deque_list = deque([i+1 for i in range(N)])

while deque_list:
    
    deque_list.rotate(-(K-1))
    result_list.append(deque_list.popleft())

# 이것도 가능
# while deque_list:

# 	for _ in range(K-1):
# 		deque_list.append(deque_list.popleft())
	
# 	result_list .append(deque_list.popleft())
    
print(f'<{", ".join(map(str,result_list))}>')