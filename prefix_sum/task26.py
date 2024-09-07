# https://leetcode.com/problems/subarray-sum-equals-k/description/

from collections import defaultdict

def solution(k, nums):
    q = 0
    psum = defaultdict(int)
    psum[0] = 1
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        q += psum[sum - k]
        psum[sum] += 1
    return q


if __name__ == "__main__":
    print(solution(int(input()), list(map(int, input().strip().split()))))
