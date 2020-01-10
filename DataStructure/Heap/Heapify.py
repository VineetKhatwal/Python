heap = [10, 20, 15, 12, 40, 25, 18]
heap_size = len(heap)


def maxHeapify(heap, i):
    l = (2 * i + 1)
    r = (2 * i + 2)
    #print(i, l, r)
    largest = i

    if (l < heap_size and heap[l] > heap[i]):
        largest = l
    if (r < heap_size and heap[r] > heap[largest]):
        largest = r
    if (largest != i):
        heap[i], heap[largest] = heap[largest], heap[i]   # Swapping
        maxHeapify(heap, largest)


def buildMaxHeap(heap):
    i = int((heap_size / 2) - 1)
    while(i >= 0):
        maxHeapify(heap, i)
        i = i - 1


buildMaxHeap(heap)
print(heap)
