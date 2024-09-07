# https://leetcode.com/problems/move-zeroes/description/

def solution(nums):
    n = len(nums)
    i = 0
    while i < n:
        if nums[i] == 0:
            nums.append(0)
            nums.remove(0)
        i += 1
    return nums


if __name__ == "__main__":
    print(solution(list(map(int, input().strip().split()))))
