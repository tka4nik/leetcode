def solution(nums1, m, nums2, n):
    for i in range(n):
        if nums1[i] > nums2[i]:
            nums1[i+1:] = nums1[i:]
            nums1[i] = nums2[i]
        else:
            nums1[i+2:] = nums1[i+1:]
            nums1[i+1] = nums2[i]
    return nums1



if __name__ == '__main__':
    print(solution(list(map(int, input().strip().split())), int(input()), list(map(int, input().strip().split())), int(input())))
