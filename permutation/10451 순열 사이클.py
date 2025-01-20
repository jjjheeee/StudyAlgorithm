'''
    10451번 "순열 사이클" 실버 3
    
    그래프 이론, 그래프 탐색, 순열 사이클 분할
    
    문제


        1부터 N까지 정수 N개로 이루어진 순열을 나타내는 방법은 여러 가지가 있다. 예를 들어, 8개의 수로 이루어진 순열 (3, 2, 7, 8, 1, 4, 5, 6)을 배열을 이용해 표현하면  
        
        [1,2,3,4,5,6,7,8]
        [3,2,7,8,1,4,5,6]
        
        와 같다. 또는, Figure 1과 같이 방향 그래프로 나타낼 수도 있다.

        순열을 배열을 이용해  
        
        
        
        로 나타냈다면, i에서 πi로 간선을 이어 그래프로 만들 수 있다.

        Figure 1에 나와있는 것 처럼, 순열 그래프 (3, 2, 7, 8, 1, 4, 5, 6) 에는 총 3개의 사이클이 있다. 이러한 사이클을 "순열 사이클" 이라고 한다.

        N개의 정수로 이루어진 순열이 주어졌을 때, 순열 사이클의 개수를 구하는 프로그램을 작성하시오.

    입력
        첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 순열의 크기 N (2 ≤ N ≤ 1,000)이 주어진다. 
        둘째 줄에는 순열이 주어지며, 각 정수는 공백으로 구분되어 있다.

    출력
        각 테스트 케이스마다, 입력으로 주어진 순열에 존재하는 순열 사이클의 개수를 출력한다.
'''
import sys

T = int(sys.stdin.readline().strip())

def check_cycle(node):
    cycle_list[node] = True
    next_node = int_list[node]
    if not cycle_list[next_node]:
        check_cycle(next_node)

for i in range(T):
    N = int(sys.stdin.readline().strip())
    cycle_list = [False for i in range(N+1)] # 0~7 까지의 index
    
    list_ = sys.stdin.readline().strip().split()
    '''
        int_list의 값이 index가 되기 때문에 리스트 길이의 최대 노드는 index out if range발생한다
        따라서 int_list의 첫값에 0을 추가하여 값과 인덱스를 맞춰준다.
        ex) N=3이면
        cycle_list = [False,False,False]
        int_list = [2,1,3]
        cycle_list, int_list에는 index=3에 해당하는값이 없기 때문에 에러가 발생한다.
    '''
    int_list = [0] + list(map(int, list_)) # 0~7 까지의 index이지만 값은 1~8까지의 정수
    
    index_list = []
    count = 0
    for i in range(1,N+1):
        if not cycle_list[i]:
            count += 1
            check_cycle(i)
        
    
    print(count)