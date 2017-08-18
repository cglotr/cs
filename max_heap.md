# Max heap

## Max-heapify

* `left(i)` and `right(i)` are assumed to satisfy max-heap property.

```
maxHeapify(A, i):
  l = left(i);
  r = right(i);

  if l < A.heap_size && A[l] > A[i]:
    largest = l;
  else:
    largest = i;

  if r < A.heap_size && A[r] > A[i]:
    largest = r;

  if largest != i:
    swap(A, i, largest);
    maxHeapify(A, largest);
```

## Build max-heap

```
buildMaxHeap(A):
  A.heap_size = A.length
  for i = (A.heap_size - 2) / 2 to 0:
    maxHeapify(A, i)
```
