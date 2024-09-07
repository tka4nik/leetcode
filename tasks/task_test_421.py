from collections import Counter


def solution(s, k, n):
    l, r = 0, 0
    sub = ""
    length = 0
    while r < n:
        sub = s[l:r]
        if sub == "" or min(Counter(sub).values()) >= k:
            length = max(length, r-l)
            r += 1
        l += 1
    return length


if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    print(solution(input(), k, n))
