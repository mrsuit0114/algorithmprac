import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = list(map(int,input().split()))
lp, rp = 0,0
ans = 0
# dic = {}
# for i in range(1,100001):  # 키값이 500개가 최대인데?
#     dic[i] = [0]  #  모든 value[0]은 해당 원소의 갯수, 이후 나온 idx저장

dic = [[0] for i in range(100001)]

while rp<n:
    value = arr[rp]
    if dic[value][0]<m:
        dic[value][0]+=1
        dic[value].append(rp)
        rp+=1
    else:
        ans = max(ans, rp-lp)
        dic[value][0]-=1
        lp = dic[value].pop(1)+1
        rp+=1

ans = max(ans, rp-lp)

print(ans)



# m만큼 겹친 원소가 어디 idx에 저장되어있는지 알아야함