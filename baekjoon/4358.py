import heapq
import sys

input= sys.stdin.readline

dic = {}
cnt=0

while True:
    s = input().rstrip()
    if s == "": # input값이 없다면 break
        break
    cnt += 1
    if s in dic: # 딕셔너리에 키가 있는지 확인
        dic[s] += 1
    else: 
        dic[s] = 1 #

dic = sorted(dic.items())


for val, key in dic:
    num = (key/cnt)*100.0
    if int(num) //2 ==0:
        num = num + 0.0005
    print(val, round(num, 4))
