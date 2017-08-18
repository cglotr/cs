# Quicksort

* `O(nlogn)` time.
* `O(logn)` space due to recursion memory requirement. In-place.

## Partition

```
partition(A, p, r):
    pivot = A[r];
    a = p;

    for b = p to r - 1:
        if A[b] <= pivot:
            swap(A, b, a);
            a++;

    swap(A, a, r);
    return a;
```

## Quicksort

```
quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r);
        quicksort(A, p, q - 1);
        quicksort(A, q + 1, r);
```
