def solution(x, y):
    x = int(x)
    y = int(y)
    ans = 0
    while x >= 1 and y >= 1:
        mx = max(x, y)
        mn = min(x, y)
        if mn == 1:
            ans += mx - mn
            return str(ans)
        ans += mx // mn
        x = mx % mn
        y = mn
    return "impossible"
