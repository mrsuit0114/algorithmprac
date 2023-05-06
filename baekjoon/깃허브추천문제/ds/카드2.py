import sys
input = sys.stdin.readline

n = int(input())

arr = list(range(1,n+1))

while len(arr)!=1:
    if len(arr)%2:
        arr = arr[1::2]  # deque는 슬라이싱이안되네
        # 앞에원소 제일 뒤로 보내기
        tmp = arr.pop(0)
        arr.append(tmp)
    else:
        arr = arr[1::2]

print(arr[0])