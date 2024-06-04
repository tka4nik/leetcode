# https://leetcode.com/problems/container-with-most-water/description/
def solution(nums):
    max_area = 0
    low = 0
    high = len(nums) - 1
    while low != high:
        max_area = max(max_area, min(nums[low], nums[high]) * (high - low))
        if nums[low] < nums[high]:
            low += 1
            continue
        if nums[low] >= nums[high]:
            high -= 1
            continue
    return max_area


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    print(solution(nums))
