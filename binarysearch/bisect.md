#### Bisect left

```py
def bisect_left(arr, x):
  n = len(arr)
  lo = 0
  hi = n
  
  while lo < hi:
    mid = lo + (hi - lo) // 2
    if arr[mid] < x:
      lo = mid + 1
    else:
      hi = mid
      
  return lo
```

#### Bisect right

```py
def bisect_right(arr, x):
  n = len(arr)
  lo = 0
  hi = n
  
  while lo < hi:
    mid = lo + (hi - lo) // 2
    if arr[mid] > x:
      hi = mid
    else:
      lo = mid + 1
      
  return lo
```
