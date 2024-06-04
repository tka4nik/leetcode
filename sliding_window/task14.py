# https://leetcode.com/problems/repeated-dna-sequences/description/
def solution(s):
    dnaset = set()
    res = set()
    for i in range(len(s) - 10 + 1):
        subseq = s[i:i + 10]
        if subseq not in dnaset:
            dnaset.add(subseq)
        else:
            res.add(subseq)
    return res


if __name__ == '__main__':
    print(solution(input()))
