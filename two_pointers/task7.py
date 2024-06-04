# https://leetcode.com/problems/3sum/
def solution(nums):
    nums = sorted(nums)
    res = set()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        low = i + 1
        high = len(nums) - 1
        while low < high:
            if nums[i] + nums[low] + nums[high] == 0:
                res.add((nums[i], nums[low], nums[high]))
                low += 1
            if nums[i] + nums[low] + nums[high] > 0:
                high -= 1
            if nums[i] + nums[low] + nums[high] < 0:
                low += 1

    return res


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    print(solution(nums))
