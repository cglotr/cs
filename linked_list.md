# Linked List

* `head` - First item in the chain. `L.head == null` means that the chain is empty.
* `tail` - Last item in the chain. If `x.next == null`, then `x` is the tail.

## Doubly linked list

* `next` - Pointer to the next item.
* `prev` - Pointer to the previous item.

### List search

```
listSearch(L, key):
    x = L.head;

    while x != null && x.key != key:
        x = x.next;

    return x;
```

### List Delete

```
listDelete(L, x):
    if x.prev != null:
        x.prev.next = x.next;
    else:
        L.head = x.next;

    if x.next != null:
        x.next.prev = x.prev;
```

### List insert

```
listInsert(L, x):
    x.next = L.head;

    if L.head != null:
        L.head.prev = x;

    L.head = x;
    x.prev = null;
```

## Doubly linked list with sentinel

* Sentinel removes the need for boundary case checking.
* Remove the need for `head` and `tail`.
* `L.nil` acts as both `head` and `tail`.
* `L.nil.next` points to the `head`.
* `L.nil.prev` points to the `tail`.

### List search with sentinel

```
listSearchWithSentinel(L, key):
    x = L.nil.next;

    while x != null && x.key != key:
        x = x.next;

    return x;
```

### List Delete with sentinel

```
listDeleteWithSentinel(L, x):
    x.prev.next = x.next;
    x.next.prev = x.prev;
```

### List insert with sentinel

```
listInsertWithSentinel(L, x):
    x.next = L.nil.next;
    L.nil.next.prev = x;
    L.nil.next = x;
    x.prev = L.nil;
```
