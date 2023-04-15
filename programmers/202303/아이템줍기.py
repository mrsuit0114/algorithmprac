from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    maps = [[-1 for i in range(15)] for i in range(15)]  # 50으로 고쳐서내야함
    

    for rec in rectangle:
        x1,y1,x2,y2 = rec

        for i in range(y1,y2+1):
            for j in range(x1,x2+1):
                maps[i][j] = 0

    dq = deque([(characterX,characterY)])
    
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    


    return answer

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],1,3,7,8))

# from collections import deque

# def solution(rectangle, characterX, characterY, itemX, itemY):
#     answer = 0

#     maps = [[-1 for i in range(15)] for i in range(15)]  # 50으로 고쳐서내야함
    

#     for rec in rectangle:
#         x1,y1,x2,y2 = rec

#         for i in range(y1,y2+1):
#             for j in range(x1,x2+1):
#                 maps[i][j] = 0

#     dq = deque([(characterX,characterY)])
    
#     dx = [0,0,-1,1]
#     dy = [1,-1,0,0]

#     def isIn(x,y,maps):
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if 0<= nx <50 and 0<= ny <50 and maps[ny][nx]==-1:
#                 return True
#         return False

#     #현재 x,y를 입력받고 다음으로 갈 지점을 리턴
#     def nextToGo(x,y,maps):  # cur에서 갈수있는곳은 어차피 한곳임
#         #교차거나 아니거나 다음지점의 인접한점이 -1이 있는지 없는지
#         #즉 다음으로가려면 다음의 다음지점들을 확인해봐야함
#         #다음지점은 0이어야하고 다음지점의 인접한점은 -1이 존재해야함
#         for i in range(4):
#             nx = x+ dx[i]        
#             ny = y+ dy[i]

#             if 0<= nx <50 and 0<= ny <50 and isIn(nx,ny,maps):
#                 return [nx,ny]


#     while dq :
#         cur = dq.popleft()
#         x = cur[0]
#         y = cur[1]
#         if x == itemX and y == itemY:
#             break

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0<= nx <50 and 0<= ny <50 and maps[ny][nx] == 0:  # 
#                 #  여기서 실제로 갈 수 있는 지점을 알아야함
#                 rx,ry = nextToGo(nx,ny,maps)
#                 maps[ry][rx] = maps[y][x]+1
#                 dq.append((rx,ry))

#     answer = maps[itemY][itemX]

#     return answer

# print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],1,3,7,8))