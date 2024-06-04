# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
def solution(nums):
    if not nums:
        return 0
    max_profit = 0
    min_price = nums[0]
    for num in nums:
        if num < min_price:
            min_price = num
        if num >= min_price:
            max_profit = max(max_profit, num - min_price)
    return max_profit


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    print(solution(nums))
