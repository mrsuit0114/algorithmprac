def solution(sizes):
    answer = 0
    lmax = 0
    hmax = 0
    for size in sizes:
        if lmax != max(lmax,*size):
            lmax = max(lmax,*size)
            hmax = min(size)
    for size in sizes:
        hmax = max(hmax,min(size))
    #가장 긴걸 눕히고 전체돌면서 둘중 작은값을 높이 max로 갱신
    answer = lmax*hmax
    return answer

solution([[60, 50], [30, 70], [60, 30], [80, 40]])