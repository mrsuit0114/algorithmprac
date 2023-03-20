from itertools import product
import math


def solution(numbers):
    answer = 0
    def sosus():
        n=1000
        array = [True for i in range(n + 1)]

        for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
            if array[i] == True: # i가 소수인 경우 (남은 수인 경우)
                # i를 제외한 i의 모든 배수를 지우기
                j = 2 
                while i * j <= n:
                    array[i * j] = False
                    j += 1
        return [i for i in range(1,len(array)) if array[i]==True ]

    

    return answer

solution("123")