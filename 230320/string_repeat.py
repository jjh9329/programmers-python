def solution(my_string, n):
    answer = ''
    for i in my_string :
        answer += i*n
    return answer
print(solution('sdkljfosida',3))