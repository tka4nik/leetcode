# https://leetcode.com/problems/valid-palindrome/description/
def solution(str):
    str = [i for i in str.strip().lower() if i.isalnum()]

    for i in range(len(str)):
        if str[i] != str[len(str)-1-i]:
            return False
    return True

if __name__ == '__main__':
    print(solution(input()))
