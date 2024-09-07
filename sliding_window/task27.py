# https://leetcode.com/problems/permutation-in-string/description/
from collections import defaultdict, Counter


def solution(s1, s2):
    d1 = defaultdict(int)
    d2 = dict(Counter(s1))
    i, j = 0, 0
    # Skip
    pass


if __name__ == "__main__":
    print(solution(input(), input()))
