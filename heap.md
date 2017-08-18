# Heap

* Binary tree with extra property.
* Types:
  * Max.
  * Min.

## Parent, left, and right indices

```
parent(i)
  return (i - 1) / 2;
```

```
left(i)
  return 2 * i + 1;
```

```
right(i)
  return 2 * i + 2;
```

## Max-heap property

```
A[parent(i)] >= A[i]
```

## Min-heap property

```
A[parent(i)] <= A[i]
```
