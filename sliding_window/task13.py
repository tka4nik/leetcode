def solution(s):
    setsubstr = set()
    res = 0

    i = 0
    for j in range(len(s)):
        while s[j] in setsubstr:
            setsubstr.remove(s[i])
            i += 1
        setsubstr.add(s[j])
        res = max(res, len(setsubstr))
    return res


if __name__ == '__main__':
    print(solution(input()))
