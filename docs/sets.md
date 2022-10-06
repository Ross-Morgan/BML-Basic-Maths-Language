# Sets

## Create a definite set from literal data points

```python
set <name> = { 1, 2, 3, 4, 5 }
```

## Create an infinite set from an expression

```python
# Set of every integer
set <name> = for (k exists `z)
             k
```

## Builtins

Some sets come predefined, such as:
- `z - set of all integers
- `c - set of all complex numbers
- `r - set of all real numbers


## Application

We can use this to create sets such as those of all odd or even numbers

```python
set even = for (k exists `z)
           k / 2 exists `z

set odd = for (k exists `z)
          (k + 1) / 2 exists `z
```