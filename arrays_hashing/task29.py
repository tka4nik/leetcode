# https://leetcode.com/problems/merge-intervals/description


def solution(intervals):
    out = []
    for interval in sorted(intervals, key=lambda i: i[0]):
        if out and interval[0] <= out[-1][1]:
            out[-1][1] = max(out[-1][1], interval[1])
        else:
            out.append(interval)
    return out


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    intervals = [[1,4],[4,5]]
    print(solution(intervals))
