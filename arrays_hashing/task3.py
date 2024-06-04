import collections

# https://leetcode.com/problems/top-k-frequent-elements/description/
def solution(nums, k):
    m = collections.Counter(nums)
    m_s = sorted(m.items(), key=lambda item: item[1], reverse=True)
    return [item[0] for item in m_s][:k]


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    k = int(input())
    print(solution(nums, k))
