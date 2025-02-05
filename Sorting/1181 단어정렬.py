'''
    1181번 "단어 정렬" 실버 5
    
    문자열, 정렬 
    
    문제
    알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

    길이가 짧은 것부터
    길이가 같으면 사전 순으로
    단, 중복된 단어는 하나만 남기고 제거해야 한다.

    입력
        첫째 줄에 단어의 개수 N이 주어진다. 
        (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 
        주어지는 문자열의 길이는 50을 넘지 않는다.

    출력
        조건에 따라 정렬하여 단어들을 출력한다.
'''

N = int(input())

words = []
for _ in range(N):
    words.append(input())
    
words = list(set(words))

words.sort()
words.sort(key=lambda word:len(word))

for i in words:
    print(i)
    
    
# import sys

# N = int(sys.stdin.readline())
# words = {sys.stdin.readline().strip() for _ in range(N)}  # 중복 제거와 개행 제거

# sorted_words = sorted(words, key=lambda word: (len(word), word))  # 길이 및 사전순 정렬

# print("\n".join(sorted_words))  # 한번에 출력