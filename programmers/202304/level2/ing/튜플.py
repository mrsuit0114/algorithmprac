def solution(s):
    answer = []
    dic ={}
    answer = s[1:-1].split(',')

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))

# 순서를 믿을수 없으므로 갯수가 작은것부터 참고해서 넣으면 해당 튜플을 알 수 있다는 것인데
# 중복된 원소는 없다고했고
# 길이 오름차순 정렬하고 새로나온 원소를 뒤에다 붙히는 식 새로나온 원소가 뭔지 알아내고 찾는것도 문제야
# 문자열을 어떻게 배열로 만들지도 문제고
