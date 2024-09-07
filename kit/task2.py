from collections import defaultdict


def solution(s):
    sum = 0
    for i in range(len(s) - 1):
        sum += abs(ord(s[i]) - ord(s[i + 1]))
    return sum


if __name__ == '__main__':
    print(solution(input()))
