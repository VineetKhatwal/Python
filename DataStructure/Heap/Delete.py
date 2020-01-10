
def maxHeapify(heap, i):
    l = (2 * i + 1)
    r = (2 * i + 2)
    largest = i

    if (l < heap_size and heap[l] > heap[i]):
        largest = l
    if (r < heap_size and heap[r] > heap[largest]):
        largest = r
    if (largest != i):
        heap[i], heap[largest] = heap[largest], heap[i]   # Swapping
        maxHeapify(heap, largest)


def delete(heap, heap_size):

    lastElem = heap[heap_size - 1]
    heap[0] = lastElem
    heap_size = heap_size - 1

    i = int((heap_size / 2) - 1)
    while(i >= 0):
        maxHeapify(heap, i)
        i = i - 1

    return heap_size


heap = [10, 20, 15, 12, 40, 25, 18]
heap_size = len(heap)

i = int((len(heap) / 2) - 1)
while(i >= 0):
    maxHeapify(heap, i)
    i = i - 1
print("**********        HEAP        **********")
print(heap)

heap_size = delete(heap, heap_size)

print("**********        HEAP        **********")
for i in range(heap_size):
    print(heap[i], end=" ")
print()
