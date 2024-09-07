# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/


def solution(nums):
    start = 0
    end = 0
    zeroes = 0
    answer = 0
    while end < len(nums):
        if nums[end] == 0:
            zeroes += 1

        while zeroes > 1:
            if nums[start] == 0:
                zeroes -= 1
            start += 1
        answer = max(answer, end - start)
        end += 1
    return answer - 1 if answer == len(nums) else answer



if __name__ == "__main__":
    print(solution(list(map(int, input().strip().split()))))
