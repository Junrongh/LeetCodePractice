如何快速建立一个长宽已知的全为0的list：


	(m, n) = len(matrix), len(matrix[0])
	zeros = [[0] * n for row in range(0, m)]
	
List 排序

	list.sort(reverse = True)
	list.sort(reverse = False) # list.sort()
	
Find K Pairs with Smallest Sums

-	Important:

heap.heappush() 时注意重复事项即矩阵中