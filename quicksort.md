# Quicksort

* `O(nlogn)` time.
* `O(logn)` space due to recursion memory requirement (in-place).

```
quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

partition(A, p, r):
    pivot = A[r]
    i = p - 1
    for j = p to r - 1:
        if A[j] <= pivot:
            i += 1
            swap(A, i, j)
    swap(A, i + 1, r)
    return i + 1
```
