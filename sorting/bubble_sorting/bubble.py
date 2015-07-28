def bubble_sort(li):
	length = len(li)
	for i in range(length - 1, 1, -1):
		for j in range(0, i):
			if li[j] > li[j+1]:
				li[j+1],li[j] = li[j], li[j+1]