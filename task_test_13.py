def solution(n, s):
    suffixes = [s[i:] for i in range(n)]
    return min(suffixes)



if __name__ == '__main__':
    print(solution(int(input()), input()))
