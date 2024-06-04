# https://leetcode.com/problems/contains-duplicate/description/
def solution(array):
    s_array = set()
    for item in array:
        if item in s_array:
            return True
        s_array.add(item)
    return False


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input = list(map(int, file.readlines()[0].split()))
    print(solution(input))
