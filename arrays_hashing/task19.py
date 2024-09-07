# https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150

from collections import defaultdict


def solution(nums):
    d = defaultdict()
    n = len(nums)
    for element in nums:
        if element not in d:
            d[element] = 0
        d[element] += 1
        if d[element] > n / 2:
            return element


if __name__ == '__main__':
    print(solution(list(map(int, input().strip().split()))))
