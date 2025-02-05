'''
    25305번 "커트라인" 브론즈 2
    
    구현, 시물레이션
    
    문제
        2022 연세대학교 미래캠퍼스 슬기로운 코딩생활에 
        $N$명의 학생들이 응시했다.

        이들 중 점수가 가장 높은 
        $k$명은 상을 받을 것이다. 이 때, 상을 받는 커트라인이 몇 점인지 구하라.

        커트라인이란 상을 받는 사람들 중 점수가 가장 가장 낮은 사람의 점수를 말한다.

    입력
        첫째 줄에는 응시자의 수 
        $N$과 상을 받는 사람의 수 
        $k$가 공백을 사이에 두고 주어진다.

        둘째 줄에는 각 학생의 점수 
        $x$가 공백을 사이에 두고 주어진다.

    출력
        상을 받는 커트라인을 출력하라.
'''

import sys

N,k = map(int,sys.stdin.readline().strip().split())

list_ = list(map(int,sys.stdin.readline().strip().split()))

def find_num(arr):
    if len(arr) <= 1:
        return arr
    
    default_num = arr[0] 
    left, equal, right = [], [], []
    
    for i in arr:
        
        if i > default_num:
            left.append(i)
        elif i < default_num:
            right.append(i)
        else:
            equal.append(i)
    return find_num(left) + equal + find_num(right)

sorted_list = find_num(list_)


print(sorted_list[k-1])