def solution(s, skip, index):
    answer = ''
    for i in s:
        tmp = i
        for k in range(index):
            tmp = chr(ord(tmp)+1)
            if 'z'<tmp:
                tmp = 'a'
            while tmp in skip:
                tmp = chr(ord(tmp)+1)
                if 'z'<tmp:
                    tmp = 'a'
        answer+=tmp
    return answer

print(solution('aukks','wbqd',5))