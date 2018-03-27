def kSmallestPairs(nums1, nums2, k):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type k: int
    :rtype: List[List[int]]
    """
    listcomp = []
    m, n = len(nums1), len(nums2)
    if m == 0 or n == 0 or k == 0:
        return []
    i = j = count = 0
    anslist = []
    complist = []
    heapq.heappush(complist, (nums1[i] + nums2[j], i, j))
    
    while count < min(m * n, k):
        ans, i, j = heapq.heappop(complist)
        anslist.append([nums1[i], nums2[j]])
        count += 1
        if i < m - 1 and j == 0: # Important: (and j == 0) to get rid of repeatance
            heapq.heappush(complist, (nums1[i + 1] + nums2[j], i + 1, j))
        if j < n - 1:
            heapq.heappush(complist, (nums1[i] + nums2[j + 1], i, j + 1))
    return anslist