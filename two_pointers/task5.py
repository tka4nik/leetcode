# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
def solution(nums, k):
    low = 0
    high = len(nums) - 1
    while low != high:
        if nums[low] + nums[high] == k:
            return [low+1, high+1]
        if nums[low] + nums[high] < k:
            low += 1
        if nums[low] + nums[high] > k:
            high -= 1


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    k = int(input())
    print(solution(nums, k))
