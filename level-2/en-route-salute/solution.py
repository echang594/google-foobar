def solution(s):
    total = 0
    right = 0
    for i in s:
        if i == ">":
            right += 1
        elif i == "<":
            total += right * 2
    return total
