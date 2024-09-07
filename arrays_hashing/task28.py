# leetcode.com/problems/maximize-distance-to-closest-person/description/


def solution(seats):
    i, j = 0, 0
    m = 1
    while j < len(seats):
        if seats[j] == 1:
            if seats[i] == 0:
                m = max(m, j)
            else:
                m = max(m, (j - i) // 2)
            i = j
        j += 1
    if seats[j - 1] == 0 and seats[i] == 1:
        m = max(m, j - 1 - i)
    return m


if __name__ == '__main__':
    print(solution(list(map(int, input().strip().split()))))
