# Difference

For any set, difference returns unique values from each set

## Example

```python
set set_a = {1, 2, 3, 4}
set set_b = {3, 4, 5, 6}
set set_c = {5, 6, 7, 8}

set_a difference set_b  # {1, 2, 5, 6}
set_b difference set_c  # {3, 4, 7, 8}
set_c difference set_a  # {1, 2, 3, 4, 5, 6, 7, 8}
```