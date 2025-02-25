'''
    2204번 "도비의 난독증 테스트" 브론즈 1
    
    문자열, 정렬
    
    문제
        꿍은 도비에게 영어단어들을 제시한 후 어떤 단어가 대소문자를 구분하지 않고 사전순으로 가장 앞서는지 맞추면 양말을 주어 자유를 얻게해준다고 하였다.

        하지만 인성이 좋지 않은 꿍은 사실 그러고 싶지 않았기 때문에 대소문자를 마구 섞어가며 단어들을 제시했다.
        예를 들어, apPle은 Bat보다 앞서지만 AnT보다는 뒤에 있는 단어다.

        도비에게 희망은 여러분뿐이다! 여러분이 도비에게 자유를 선물해주도록 하자!

    입력
        각 테스트케이스는 정수 n (2 ≤ n ≤ 1000) 으로 시작하며 주어지는 단어의 개수를 뜻한다.

        다음 각 n줄은 길이가 최대 20인 단어가 주어지며 대소문자의 구분을 없앴을 때 똑같은 단어는 주어지지 않는다.

        마지막 입력은 0이 주어진다.

    출력
        각 줄에 각 테스트케이스에서 사전상 가장 앞서는 단어를 출력한다.
'''
import sys

while True:
    
    n = int(sys.stdin.readline().strip())
    
    if n == 0:
        break
    
    temp_list = []
    for i in range(n):
        word = sys.stdin.readline().strip()
        lower_word = word.lower()
        temp_list.append([lower_word, word]) 	
        
    temp_list.sort()
    print(temp_list[0][1])