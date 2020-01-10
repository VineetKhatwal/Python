heap = []


def insert(key):
    heap.append(key)
    i = len(heap) - 1
    p = parent(i)

    while (i >= 0 and heap[p] < heap[i]):
        heap[p], heap[i] = heap[i], heap[p]
        i = p
        p = parent(p)


def parent(x):
    return int((x - 1) / 2)


def maxHeapify(heap, i):
    l = (2 * i + 1)
    r = (2 * i + 2)
    largest = i

    if (l < len(heap) and heap[l] > heap[largest]):
        largest = l
    if (r < len(heap) and heap[r] > heap[largest]):
        largest = r
    if (largest != i):
        heap[i], heap[largest] = heap[largest], heap[i]   # Swapping
        maxHeapify(heap, largest)


def heapify(heap):
    i = int((len(heap) / 2) - 1)
    while(i >= 0):
        maxHeapify(heap, i)
        i = i - 1


def delete(heap):

    heap_size = len(heap) - 1
    heap[0] = heap[heap_size]
    heapify(heap)
    return heap_size


arr = [10, 20, 99, 15, 30, 23, 40]
for i in range(len(arr)):
    insert(arr[i])
# insert(23)
# insert(99)
print("**********        HEAP        **********")
print(heap)

heap = [10, 20, 99, 15, 30, 23, 40]
heapify(heap)
print("**********        HEAP        **********")
print(heap)

heap_size = delete(heap)

print("**********        HEAP        **********")
for i in range(heap_size):
    print(heap[i], end=" ")
print()

print("**********        Max Element  : O(1)      **********")
print(heap[0])

print("**********        Min Element  : O(1)      **********")
print(heap[len(heap) - 1])
