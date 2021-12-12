def merge(nums1, m, nums2, n) -> None:
    index1, index2 = m - 1, n - 1
    for i in range(len(nums1) - 1, -1, -1):
        val1 = nums1[index1] if index1 >= 0 else float('-inf')
        val2 = nums2[index2] if index2 >= 0 else float('-inf')
        if val1 >= val2:
            nums1[i] = val1
            index1 -= 1
        else:
            nums1[i] = val2
            index2 -= 1

merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)