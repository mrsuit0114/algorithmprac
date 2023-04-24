def solution(arr):
    answer = 0
    dp = [[0,-1]]
    rcount = 0
    for r in range(1,len(arr)+1):
        
        for row in range(4):
            

    return answer

# i행까지 최댓값인 루트를 탔을 때 i+1행까지 최댓값인 루트가 겹치지 않을수도있음
# dp 써야하나 i+2를 구하기위해서 i+1과 i를 참고해야함
# i+1에서는 이전 열만 빼면 최댓값을 취하면되지만 i에서는 arr[i]와 arr[i+1]에서 값을 참고해서 밟아야함




