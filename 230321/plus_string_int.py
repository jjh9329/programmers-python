def solution(my_string):
    result=0
    for i in my_string:
        if i.isnumeric():
            result+=int(i)
    answer = result
    return answer
#다른사람의 풀이
def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())