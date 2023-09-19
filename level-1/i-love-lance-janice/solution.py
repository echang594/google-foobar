def solution(x):
    s = ""
    for i in x:
        if i.islower():
            s += chr(ord("z") - ord(i) + ord("a"))
        else:
            s += i
    return s
