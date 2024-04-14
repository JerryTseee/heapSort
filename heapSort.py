"""
Heap data structure
1. max-heap (A[parent(i)] >= A[i])
2. min-heap (A[parent(i)] <= A[i])
"""

"""

parent(i){ return i//2 }

left(i){ return 2i }

right(i){ return 2i+1 }



1. max-heap pseudo code

max-heap(A,i){
    l = left(i)
    r = right(i)

    if A[l] > A[i]: largest = l
    else: largest = i

    if A[r] > A[largest]: largest = r

    if largest != i:
        exchange A[i] and A[largest]
        max-heap(A, largest)
}




2. min-heap pseudo code

min-heap(A,i){
    l = left(i)
    r = right(i)

    if A[l] < A[i]: smallest = l
    else: smallest = i

    if A[r] < A[smallest]: smallest = r

    if smallest != i:
        exchange A[i] and A[smallest]
        max-heap(A, smallest)
}
"""

def heapSort(arr):
    length = len(arr)

    #build a max-heap
    for i in range(length//2-1, -1, -1):
        max-heap(arr, i)

    #one by one extract the elements, put the largest elements into the sorted output
    for i in range(length-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max-heap(arr, i)