heap_size = 0
heap = []


def insert(key):

    global heap_size
    heap.append(key)
    heap_size += 1
    i = heap_size - 1
    p = parent(i)

    while (i >= 0 and heap[p] < heap[i]):
        heap[p], heap[i] = heap[i], heap[p]
        #swap(heap, p,i)
        i = p
        p = parent(p)


def parent(x):
    return int((x - 1) / 2)


def swap(heap, x, y):
    temp = heap[x]
    heap[x] = heap[y]
    heap[y] = temp


arr = [10, 20, 15, 30, 40]
for i in range(len(arr)):
    insert(arr[i])
insert(23)
insert(99)
print(heap)
