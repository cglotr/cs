# Bit manipulation

## Operators

|Symbol         |Operation             |
|---------------|----------------------|
|~              |NEGATION              |
|\|             |OR                    |
|&              |AND                   |
|^              |XOR                   |

## Truth tables

**NEGATION (~)**

|Input       |Output      |
|------------|------------|
|0           |1           |
|1           |0           |

**OR (|)**

|Input 1     |Input 2     |Output      |
|------------|------------|------------|
|0           |0           |0           |
|0           |1           |1           |
|1           |0           |1           |
|1           |1           |1           |

**AND (&)**

|Input 1     |Input 2     |Output      |
|------------|------------|------------|
|0           |0           |0           |
|0           |1           |0           |
|1           |0           |0           |
|1           |1           |1           |

**XOR (^)**

|Input 1     |Input 2     |Output      |
|------------|------------|------------|
|0           |0           |0           |
|0           |1           |1           |
|1           |0           |1           |
|1           |1           |0           |

## Notable results

**OR (|)**

|              |              |
|--------------|--------------|
|x ^ 0...0     |x             |
|x ^ 1...1     |~x            |
|x ^ x         |0...0         |

**AND (&)**

|              |              |
|--------------|--------------|
|x & 0...0     |0...0         |
|x & 1...1     |x             |
|x & x         |x             |

**XOR (^)**

|              |              |
|--------------|--------------|
|x \| 0...0    |x             |
|x \| 1...1    |1...1         |
|x \| x        |x             |

## Bit tasks

**Set**

```
setBit(bits, i)
  bits | (1 << i)
```

**Clear**

```
clearBit(bits, i)
  bits & ~(1 << i)
```

**Update**

```
updateBit(bits, i, bit)
  bits & ~(1 << i)
  bits | (bit << i)
```

**Clear (from left most to i)**

```
clearLeftBits(bits, i)
  bits & ((1 << i) - 1)
```

**Clear (from right most to i)**

```
clearRightBits(bits, i)
  bits & ~((1 << (i + 1)) - 1)
```
