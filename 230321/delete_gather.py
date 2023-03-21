def solution(my_string):
    gather = ['a','e','i','o','u']
    for i in my_string:
        print(i)
        if i in gather :
            print('i가 gater안에 있다')
            my_string = my_string.replace(i,'') # 그냥 my_string.replace(i,'')로 만하면 return my_string 할시 bus가 출력되는대
            #my_string 에 다시 담아줄시 return값은 bs가 된다.
            print(my_string)
    return my_string

#다른사람의 풀이
def solution(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])
print(solution('nice to meet you'))