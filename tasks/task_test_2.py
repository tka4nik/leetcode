def solution(nums):
    return nums.index(max(nums)) + 1


if __name__ == '__main__':
    n = int(input())
    print(solution(tuple(map(int, input().strip().split()))))
