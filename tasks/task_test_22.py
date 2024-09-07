def solution(n, nums):
    def dfs(nums, profit):
        if len(nums) == 0:
            return profit
        choices = [i for i in range(len(nums))]
        profits = []
        for i in choices:
            nums_new = nums.copy()
            tmp = nums_new[i]
            nums_new.remove(nums_new[i])
            if not nums:
                profits.append(profit)
            while nums_new[i]+1 in nums_new:
                nums_new.remove(nums_new[i]+1)

            while nums_new[i]-1 in nums_new:
                nums_new.remove(nums_new[i]-1)

            profits.append(dfs(nums_new, profit+tmp))
        return max(profits)

    return dfs(nums, 0)


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().strip().split()))
    print(solution(n, nums))



