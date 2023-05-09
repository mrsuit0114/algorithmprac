import sys

input = sys.stdin.readline

n = int(input())
ans = []
stk = []
# brk = 0  #스택의 제일 위의 원소
count = 1

for i in range(n):
    tmp = int(input())
    for j in range(count,n+1):
        if j<tmp:
            ans.append("+")
            brk = j
        elif j==tmp:
            ans.append("+")
            ans.append("-")
            # 이후 나가서 다시 입력받고 나중에 다시 올때는 마지막으로 했던 상황이후부터 시작해야지
            count = j+1
            break
        else:  # 작을 때
            if tmp==brk:
                ans.append("-")
                brk -= 1
                break
            else:
                print("NO")
                exit(0)
print(*ans,sep="\n")

            





# 1부터 n까지 차례대로 주어지는상황에서 스택의 팝과 푸시를 적절히 이용하여
# 1부터 n까지 임의의 순서대로 주어지는 수열과 일치시킬 수 있는지알아보고
# 가능하면 +(푸시), -(팝)으로 나타내라

# 팝하고 다음값이 작을 때 가장 마지막에 팝했던 값보다 1작은값이 아니라면 불가능,
# 큰거는 얼마나 커도 상관없는데
# 일단 처음에는 해당 값만큼 + 하고 다음값이 커지는동안 계속 + 작아지면

