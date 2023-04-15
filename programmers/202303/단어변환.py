from collections import deque

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    
    num = len(words)
    visit = [0]*(num+1)
    words.append(begin)

    dq=deque([num])  # 가능한 단어의 idx
    cur = ""  # 현재 단어

    def isOneDiff(cur,word):  # 현재 변환 가능한 단어인지 확인
        flag = 0
        for i in range(len(word)):
            if word[i] != cur[i]:
                flag+=1
        return True if flag==1 else False
    
    while dq :  # dqempty 여부를확인해야하는데 어떻게 처리할까
        curIdx = dq.popleft()
        cur = words[curIdx]
        if cur == target :
            answer = visit[curIdx]
            break
        for i in range(len(words)):
            if isOneDiff(cur,words[i]) and visit[i]==0:
                dq.append(i)
                visit[i] = visit[curIdx]+1
            

    return answer

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"] ))

from collections import deque


def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):  # 알파벳 하나씩 비교하기위한 zip
            if c != w:
                count += 1

        if count == 1:
            yield word  #  배열과 자동으로 참조하는 iterator를 세트로주는 느낌


def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])  # 알고리즘 돌리기위해 dq에 초반값을 넣고 쇼를했는데 idx 추가하고.. //  이런방식으로 가능하네

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):  # 이미 방문했던곳도 또 가는건아닌지?
            if next_word not in dist:  # 여기서 방문을 확인하네
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)  # 있으면 target의 value  없으면 default값으로 지정한 0