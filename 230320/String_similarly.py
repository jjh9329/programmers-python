def solution(s1, s2):
    answer = 0
    for a in s1 :
        for b in s2:
            if(a == b):
                answer +=1
            
    return answer

s1=["a", "b", "c"]
s2=["com", "b", "d", "p", "c"]

# set(s1)&set(s2) => s1과 s2의 교집합  set(s1)|set(s2) => s1과 s2의 합집합
print(solution(s1,s2))