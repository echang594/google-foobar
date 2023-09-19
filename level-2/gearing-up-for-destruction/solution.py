from __future__ import division


def solution(pegs):
    constant = 0
    for i in range(1, len(pegs)):
        constant = pegs[i] - pegs[i - 1] - constant
    if len(pegs) % 2 == 0:
        if constant % 3 == 0:
            ans = [constant * 2 // 3, 1]
        else:
            ans = [constant * 2, 3]
    else:
        ans = [constant * -2, 1]
    radius = ans[0] / ans[1]
    if not 1 <= radius <= pegs[1] - pegs[0]:
        return [-1, -1]
    for i in range(1, len(pegs)):
        radius = pegs[i] - pegs[i - 1] - radius
        if not 1 <= radius <= pegs[i] - pegs[i - 1]:
            return [-1, -1]
    return ans
