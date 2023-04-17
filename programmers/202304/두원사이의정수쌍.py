
def posInCircle(rad):
    points = 0
    lastx = rad
    intpos = 0 
    for i in range(1,rad+1): #y좌표
        #조건을 만족하는 최대 i에 +1이 해당 y에서 만족하는 정수점의 갯수
        while i**2 + lastx**2 > rad**2: #원 밖인 동안
            lastx-=1 # x좌표를 빼서 다시 계산할것
        if i**2 + lastx**2 == rad ** 2:
            intpos+=1
        #내부 최대x
        points += lastx+1
    return [points,intpos]


def solution(r1, r2):
    answer = 0
    maxr = max(r1,r2)
    minr = min(r1,r2)
    big = posInCircle(maxr)
    small = posInCircle(minr)
    answer = 4*(big[0]-small[0]+small[1])
#내부원이 좌표축외에도 정수쌍을 지나가는 경우는 포함해줘야하는데 빼서 틀린다, x=0인 정수쌍계산이 중복으로 들어가서 1빼준 계산식
#(0,0) 생각해야함! 어차피 두 원 다 가지고있기때문에 계산안해줘도됨

    return answer

solution(2,3)

# r1 > r2 : 4*(pos(r1) - pos(r2) + 1)