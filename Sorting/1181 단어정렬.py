'''
    1181번 "단어 정렬" 실버 5
    
    정렬 
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