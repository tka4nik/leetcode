# https://leetcode.com/problems/valid-parentheses/description/
def solution(str):
    stack = []
    for char in str:
        if char in "{[(":
            stack.append(char)
        else:
            if not stack or \
                    (char == ")" and stack[-1] != "(") or \
                    (char == "]" and stack[-1] != "[") or \
                    (char == "}" and stack[-1] != "{"):
                return False
            stack.pop()
    return not stack


if __name__ == '__main__':
    print(solution(input()))
