# Merge Sort

## Merge Sort

```
mergeSort(A, p, r):
    if p < r:
        q = (p + r) / 2;
        mergeSort(A, p, q);
        mergeSort(A, q + 1, r);
        merge(A, p, q, r);
```

## Merge

* `l_arr.length == (q - p + 1) + 1`. The last `+1` is due to the sentinel.
* `r_arr.length == r - q + 1`. `q` is not included. The `+1` is due to the sentinel.

```
merge(A, p, q, r):
    l_arr = [A[p...q], MAX_VALUE];
    r_arr = [A[q + 1...r], MAX_VALUE];

    l_p = 0;
    r_p = 0;

    for i = p to r:
        if l_arr[l_p] <= r_arr[r_p]:
            A[i] = l_arr[l_p++];
        else:
            A[i] = r_arr[r_p++];
```
