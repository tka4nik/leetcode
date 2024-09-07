# https://leetcode.com/problems/summary-ranges/description/


def solution(nums):
    if len(nums) == 1:
        return [str(nums[0])]

    result = []
    start = 0
    pointer = 0
    while pointer < len(nums)-1:
        if nums[pointer] + 1 != nums[pointer+1]:
            if start == pointer:
                result.append(str(nums[pointer]))
            else:
                result.append(f"{nums[start]}->{nums[pointer]}")
            start = pointer + 1
        pointer += 1

        if start == pointer and pointer + 1 == len(nums):
            result.append(str(nums[pointer]))
        elif pointer + 1 == len(nums):
            result.append(f"{nums[start]}->{nums[pointer]}")

    return result


if __name__ == "__main__":
    print(solution(list(map(int, input().strip().split()))))
