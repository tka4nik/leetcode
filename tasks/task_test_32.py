def solution(n):
    while (n//10) % 10 != 0:
        n = sum(list(map(int, str(n))))
    return n


if __name__ == '__main__':
    print(solution(int(input())))

