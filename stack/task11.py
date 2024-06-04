# def solution(nums):
#     stack = []
#     res = [0]*len(nums)
#     current = 0
#     for i in range(1, len(nums)):
#         stack.append(i)
#         while stack and nums[i] > nums[current]:
#             res[current] = len(stack)
#             stack.pop()
#             current += 1
#     print(res)

def solution(nums):
    res = [0] * len(nums)
    stack = []
    stack.append((nums[-1], len(nums) - 1))
    for i in range(len(nums) - 2, -1, -1):
        while stack and stack[-1][0] <= nums[i]:
            stack.pop()
            if not stack:
                stack.append((nums[i], i))
                break

        if stack and stack[-1][0] > nums[i]:
                res[i] = stack[-1][1] - i
                stack.append((nums[i], i))
    return res


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    print(solution(nums))
