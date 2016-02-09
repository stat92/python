'''
	Time of sorting
Bubble:   	156 ms   	
Insertion:	 95 ms
Selection:	 90 ms
Merge:		 45 ms

	Sorting Algorithms Benchmarks Comparison
http://www.youtube.com/watch?v=bJ0aERNrErA

'''

# Bubble sort
def bubble_sort(A):
	l = len(A)	
	for i in range(0,l):
		for j in range(0,l-i-1):
			if A[j] > A[j+1]:
				temp = A[j]
				A[j] = A[j+1]
				A[j+1] = temp
	return A


# Insertion sort
def insertion_sort(A):
	l = len(A)	 
	for i in range(1,l):
		temp = A[i]
		j = i-1
		while A[j] > temp and j>=0:
			A[j+1] = A[j]
			j -= 1
		A[j+1] = temp
	return A


# Selection sort
def selection_sort(A):
	l = len(A)	 
	for i in range(0,l-1):
		for j in range(i+1,l):
			if A[i] > A[j]:
				temp = A[i]
				A[i] = A[j]
				A[j] = temp
	return A


# Merge sort
def merge_sort(A):
	if len(A) <= 1:
		return A
	middle = int(len(A)/2)
	left = merge_sort(A[:middle])
	right = merge_sort(A[middle:])
	return merge(left,right)

def merge(left, right):
	result = []
	while len(left) > 0 and len(right) > 0:
		if left[0] <= right[0]:
			result.append(left[0])
			left = left[1:]
		else:
			result.append(right[0])
			right = right[1:]
	if len(left)>0:
		result += left
	if len(right)>0:
		result += right
	return result