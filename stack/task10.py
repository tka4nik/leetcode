res = []

# https://leetcode.com/problems/generate-parentheses/description/
def dfs(open, close, s, n):
    if len(s) == 2 * n:
        res.append(s)
        return

    if open < n:
        dfs(open + 1, close, s + "(", n)
    if close < open:
        dfs(open, close + 1, s + ")", n)


def solution(n):
    dfs(0, 0, "", n)
    return res


# Genius solution using stack
# def generateParenthesis(n):
#     res = []
#     s = [("(", 1, 0)]
#     while s:
#         x, l, r = s.pop()
#         if l - r < 0 or l > n or r > n:
#             continue
#         if l == n and r == n:
#             res.append(x)
#         s.append((x+"(", l+1, r))
#         s.append((x+")", l, r+1))
#     return res


if __name__ == '__main__':
    # print(solution(int(input())))
    print(generateParenthesis(int(input())))
