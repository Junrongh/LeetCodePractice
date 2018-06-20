def kthSmallest(matrix, k):
    ''''
    https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
    '''
    l = []
    for row in matrix:
        l += row
    return sorted(l)[k - 1]