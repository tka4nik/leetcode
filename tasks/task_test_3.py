def solution(num1, num2):
    bulls = 0
    cows = 0
    for ch1, ch2 in zip(num1, num2):
        if ch1 == ch2:
            bulls += 1
        elif ch2 in num1:
            cows += 1
    return bulls, cows


if __name__ == '__main__':
    print(*solution(input(), input()), sep="\n")
