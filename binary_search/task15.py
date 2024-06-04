def solution(nums, target):
    l = 0
    r = len(nums) - 1
    while l < r:
        mid = (l + r + 1) // 2
        if nums[mid] <= target:
            l = mid
        else:
            r = mid - 1
    return nums[l] if nums[l] == target else -1


if __name__ == '__main__':
    print(solution(list(map(int, input().split())), int(input())))
