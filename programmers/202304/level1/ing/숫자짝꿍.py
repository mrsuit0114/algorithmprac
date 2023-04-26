def solution(X, Y):
    answer = ''
    arrx = [0] * 10
    arry = [0] *10
    for i in str(X):
        arrx[int(i)]+=1
    
    for i in str(Y):
        arry[int(i)]+=1
    
    for j in range(9,0,-1):
        tmp = min(arrx[j],arry[j])
        answer+= str(j)*tmp
    
    tmp = min(arrx[0],arry[0])

    if answer=="" and tmp!=0:
        return "0"
    else:
        answer+="0"*tmp


    if answer=="":
        return "-1"

    return answer

