# https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150



def solution(s):
    s = s.strip().split()
    return len(s[-1])


if __name__ == '__main__':
    print(solution(input()))
