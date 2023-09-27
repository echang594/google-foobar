def solution(l):
    ans = 0
    divisors = [0] * len(l)
    for i in range(len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                divisors[i] += 1
                ans += divisors[j]
    return ans
