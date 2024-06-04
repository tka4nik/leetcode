def solution(num):
    q = 0
    while num:
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1
        q += 1
    return q


if __name__ == '__main__':
    print(solution(int(input())))