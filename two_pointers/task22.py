# https://leetcode.com/problems/string-compression/description/

from typing import List


def solution(chars: List[str]) -> int:
    pointer, group = 0, 0
    while pointer < len(chars):
        counter = 1
        while pointer + 1 < len(chars) and chars[pointer] == chars[pointer + 1]:
            chars.pop(pointer+1)
            counter += 1

        if counter > 1:
            for c in map(int, str(counter)):
                chars.insert(pointer+1, str(c))
                pointer += 1

        pointer += 1

    return len(chars)


if __name__ == "__main__":
    chars = list(input())
    print(solution(chars))
    print(chars)
