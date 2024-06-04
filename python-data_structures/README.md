# Python: data structures
In this project we are gonna learn data structures such as lists, tuples, etc.

## First things first: What do we need to know to do this?

### What are lists and how to use them
Lists are orderer collections of items, which of can be different types (such as integers, strings or even other lists). They are mutable, like, you can change, add and remove elements from them. **Lists are defined by enclosing comma-separated values within square brackets `[ ]`**

### What are the differences and similarities between strings and lists
| Feature | Strings | Lists |
| :------------------- | :----------: | ----------: |
| Type             | Sequence of characters      | Sequence of any data types       |
| Mutable              | Immutable      | Mutable     |
| Declaration               | Enclosed in single or double quotes      | Enclosed in square brackets       |
| Indexing             | Acces individual characters     | Access individual elements    |
| Slicing             | Extract substrings      | Extract sublists     |
| Concatenation              | Concatenation with `+` operator      | Concatenation with `+` operator       |
| Length            | `len()` function     | `len()` function       |
| Iteration              | Iterate over characters      | Iterate over elements     |
| Modification               | Cannot be modified      | Can be modified using various methods       |
| Use cases               | Text processing, immutable data      | Data manipulation, mutable collections       |

### What are the most common methods of lists and how to use them
- `append(item)`: Adds an item to the end of the list.
- `extend(iterable)`: Extends the list by appending elements from the iterable.
- `insert(index, item)`: Inserts an item at a specified index.
- `remove(item)`: Removes the first occurrence of the item from the list.
- `pop([index])`: Removes and returns the item at the specified index. If no index is provided, it removes and returns the last item.
- `index(item)`: Returns the index of the first occurrence of the item in the list.
- `count(item)`: Returns the number of occurrences of the item in the list.
- `sort()`: Sorts the list in ascending order.
- `reverse()`: Reverses the elements of the list in place.

### How to use lists as stacks and queues
As a stack: Use the `append()` and `pop()` methods. Items added with `append()` will be at the end of the list and can be removed with `pop()`.
As a queue: Use the `append()` method to add items to the end of the list and the `pop(0)` method to remove items from the beginning of the list.

### What are list comprehensions and how to use them
List comprehensions are a concise way to create lists in Python. They provide a compact way to generate lists from existing iterables or sequences. The syntax is `[expression for item in iterable]`.

### What are tuples and how to use them
Tuples are similar to lists, but they are immutable, meaning once they are created, their elements cannot be changed. Tuples are defined by enclosing comma-separated values within parentheses `( )`.

### When to use tuples versus lists
- Use tuples when you have a collection of items that will not change, such as coordinates or configurations.
- Use lists when you need a collection of items that can be modified, such as a list of tasks or user inputs.

### What is a sequence
A sequence refers to an ordered collection of items. Both strings and lists are examples of sequences.

### What is tuple packing
Tuple packing is the process of creating a tuple without explicitly using parentheses. For example:
```
tuple_packing = 1, 2, 3
```

### What is sequence unpacking
Sequence unpacking is the process of extracting individual elements from a sequence and assigning them to variables. For example:
```
my_list = [1, 2, 3, 4, 5]
del my_list[2]  # Deletes the item at index 2
del my_list[:]  # Deletes all items in the list
```

### What is the del statement and how to use it
The del statement in Python is used to delete objects. It can be used to remove items from lists, slices from lists, variables, or even entire slices of lists or variables. Its syntax is straightforward:
```
del target
```
Here, target can be any valid expression that refers to an object. It could be a variable, an item in a list, a slice of a list, or even an entire list itself.
