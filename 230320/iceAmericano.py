import math
def solution(money):
    americano = 5500
    answer = []
    cups=money/americano
    change= money%americano
    answer.append(math.floor(cups))
    answer.append(change)
    return answer

print(solution(30000))
