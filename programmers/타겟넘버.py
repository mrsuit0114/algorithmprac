def solution(numbers, target):
    global answer
    answer = 0
    global a
    a = [0]

    def cal(depth,numbers,target):
        b=[]
        global a
        global answer
        if depth==len(numbers)-1: #맨처음에 한번 넣으므로 한번 더빼야함 --> 맨처음이 음수인경우를 누락함
            for i in range(len(a)):
                tmp = a.pop()
                k = tmp+numbers[depth]
                t = tmp-numbers[depth]
                if t==target or k==target:
                    answer+=1
            return answer

        for i in range(len(a)):
            tmp = a.pop()
            b.append(tmp+numbers[depth])
            b.append(tmp-numbers[depth])
        a=b
        cal(depth+1,numbers,target)

    cal(0,numbers,target)

    return answer

print(solution([1, 1, 1, 1, 1],3))