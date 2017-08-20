# Greatest Common Divisor

```
gcd(a, b):
    if b == 0:
        return a;
    else:
        gcd(b, a % b);
```
