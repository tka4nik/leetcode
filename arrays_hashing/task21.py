# https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150


def solution(strs):
    sub = ""
    for i in range(strs[0]):
        sub += strs[0][i]
        


if __name__ == '__main__':
    n = int(input())
    strs = [input() for i in range(n)]
    print(solution(strs))
