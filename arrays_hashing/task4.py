# https://leetcode.com/problems/product-of-array-except-self/description/
def solution(nums):
    # Prefix and suffix mult
    prefix_mult = [0]*len(nums)
    suffix_mult = [0]*len(nums)

    prefix_mult[0] = 1
    for i in range(1, len(nums)):
        prefix_mult[i] = prefix_mult[i-1] * nums[i-1]

    suffix_mult[-1] = 1
    for i in range(len(nums)-2, -1, -1):
        suffix_mult[i] = suffix_mult[i+1] * nums[i+1]

    # print(prefix_mult)
    # print(suffix_mult)

    return [prefix_mult[i] * suffix_mult[i] for i in range(len(nums))]

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    print(solution(nums))
