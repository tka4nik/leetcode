def solution(m):
    count = 0
    for i in range(len(m) - 1, -1, -1):
        if m[i][-1] >= 0:
            break
        for j in range(len(m[0]) - 1, -1, -1):
            if m[i][j] >= 0:
                continue
            count += 1
    return count


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))

    print(solution(matrix))

