def solution(n):
    answer = 0
    num = str(n)
    for i in range(0,len(num)):
        answer += int(num[i])
    return answer

#다른 사람의 풀이
def solution(n):
    return sum(int(i) for i in str(n))
print(solution(1234))