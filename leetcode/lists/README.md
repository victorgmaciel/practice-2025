[## Lists in Python


](# Python Lists

## What is a List?
A **list** is a built-in Python data structure that holds an **ordered**, **changeable** (mutable) collection of **items**.
Lists can contain **any type** of object: numbers, strings, even other lists.

```python
my_list = [1, 2, 3, "hello", [4, 5]]
```

---

## Key Properties
- **Ordered**: Items maintain the order you insert them.
- **Mutable**: You can change, add, or remove items.
- **Allows duplicates**: Lists can contain repeated elements.

---

## Common List Operations

| Operation               | Example                     | Result                     |
|-------------------------|------------------------------|-----------------------------|
| Access by index         | `my_list[0]`                 | `1`                         |
| Slicing                 | `my_list[1:3]`               | `[2, 3]`                    |
| Change an item          | `my_list[0] = "new"`         | Updates first item          |
| Add item (append)       | `my_list.append(6)`           | Adds 6 to the end            |
| Insert item             | `my_list.insert(1, "hi")`    | Inserts "hi" at index 1      |
| Remove item (by value)  | `my_list.remove(2)`           | Removes the first)