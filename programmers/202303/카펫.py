def solution(brown, yellow):
    answer = []
    sero = 1
    garo = 1

    for i in range(1,yellow):  #세로길이
        if yellow%i == 0 and yellow%i == 0 :
            if brown == i*2 + (yellow//i)*2 +4:
                sero = i
                garo = yellow//i

    garo+=2
    sero+=2

    answer = [max(garo,sero),min(garo,sero)]
    print(answer)
    return answer

solution(10,2)

# yellow의 가로길이*2+ 세로길이*2+4 == brown의 갯수를 만족할때