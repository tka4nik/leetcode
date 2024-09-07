from collections import Counter


def solution(s, k):
    for j in range(len(s), k - 1, -1):
        for i in range(len(s) - j + 1):
            sub = s[i:j + i]
            if min(Counter(sub).values()) >= k:
                return len(sub)


if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    print(solution(input(), k))
