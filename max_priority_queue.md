# Max-priority queue

## What we can do
* `heapMaximum(A)` - Peek the current most important person.
* `heapExtractMaximum(A)` - Get the celebrity out of the queue!
* `heapIncreaseKey(A, i, key)` - Bump up our guy.
* `maxHeapInsert(A, key)` - Insert a new person to the queue.

## Heap maximum

* `O(1)` time.
* `O(1)` space.

```
heapMaximum(A):
    return A[0];
```

## Heap extract maximum

* 'O(logn)' time.
* `O(1)` space.

```
heapExtractMaximum(A):
    if A.heap_size < 1:
        throw error("heap underflow");

    max = A[0];
    A[0] = A[A.heap_size - 1];
    A.heap_size--;
    maxHeapify(A, 0);
    return max;
```

## Heap increase key

* `O(logn)` time.
* `O(1)` space.

```
heapIncreaseKey(A, i, key):
    if key < A[i]:
        throw error;

    A[i] = key;

    while i > 0 && A[parent(i)] < A[i]:
        swap(A, parent(i), i);
        i = parent(i);
```

## Max heap insert

* `O(logn)` time.
* `O(1)` space.

```
maxHeapInsert(A, key):
    A.heap_size++;
    A[A.heap_size - 1] = MIN_VALUE;
    heapIncreaseKey(A, A.heap_size - 1, key);
```
