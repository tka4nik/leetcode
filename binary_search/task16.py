# https://leetcode.com/problems/koko-eating-bananas/description/
def solution(nums, h):
    def condition(k, nums, h):
        bananas = nums.copy()
        hours = 0
        for i in range(len(bananas)):
            while bananas[i] > 0:
                bananas[i] -= k
                hours += 1
        if hours > h:
            return False
        return True

    l = 1
    r = max(nums)
    while l < r:
        mid = (l + r) // 2
        if condition(mid, nums, h):
            r = mid
        else:
            l = mid + 1
    return l


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    h = int(input())

    # print(condition(5, nums, h))
    #
    print(solution(nums, h))

