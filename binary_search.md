Errichto's binary search types ([video](https://www.youtube.com/watch?v=LcWPKR1uef4))

1.  Looking for `target` in a sorted array

    ```py
    lo = 0
    hi = n-1
    while lo <= hi:
        mid = (hi-lo)/2+lo
        if A[mid] == target:
            return mid
        else if A[mid] > target:
            hi = mid-1
        else:
            lo = mid+1
    return -1
    ```

2.  Looking for the index of the first element that satisfies some property

    ```py
    lo = 0
    hi = n-1
    while lo < hi:
        mid = (hi-lo)/2+lo
        if property(mid):
            hi = mid
        else:
            lo = mid+1
    return lo
    ```
    
    There is also `hi = n` variant if it is possible that none of the elements can satisfy the property
