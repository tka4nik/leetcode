# https://leetcode.com/problems/valid-anagram/
def solution(s, t):
    if len(s) != len(t):
        return False
    s = sorted(s)
    t = sorted(t)
    for i in range(len(s)):
        if t[i] != s[i]:
            return False
    return True
    # return collections.Counter(s) == collections.Counter(t)

if __name__ == '__main__':
    # with open('input.txt', 'r') as file:
    #     input = list(map(int, file.readlines()[0].split()))


    print(solution(input(), input()))


#