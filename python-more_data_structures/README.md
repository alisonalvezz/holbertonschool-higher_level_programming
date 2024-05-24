# Python: More data structures: Set and Dictionary
In this project we are gonna learn about data structures: 
- What are sets and how to use them
- What are the most common methods of set and how to use them too
- When to use sets and when to use lists 
- What are dictionaries and how to use them
- What is a key in a dictionary
- What is lambda function
- What are map and filter functions


### What are sets?
#### Definition: 
A set is an unordered collection of unique elements. It is similar to lists, but with no duplicate elements and no specific order.
#### Common Methods:
- **add(element):** Adds a single element to the set.
- **update(iterable):** Adds multiple elements from an iterable (such as a list or another set) to the set.
- **remove(element):** Removes a specified element from the set. Raises a KeyError if the element is not present.
- **discard(element):** Removes a specified element from the set if it is present. Does not raise an error if the element is not found.
- **pop():** Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
- **clear():** Removes all elements from the set.

#### When to Use: 
Sets are useful when you need to work with unique elements and perform set operations like union, intersection, difference, etc. They are particularly efficient for membership testing and removing duplicates from a collection.

### Lists vs Sets
- Use **lists** when you need to maintain elements in a specific order and allow duplicates.
- Use **sets** when you need to work with unique elements and don't require a specific order.

### Dictionaries
#### Definition:
A dictionary is a collection of key-value pairs. Each key is unique and maps to a corresponding value.

#### A key:
A key in a dictionary is a unique identifier for each element. It is used to access the corresponding value in the dictionary.
#### Common Methods:
- **get(key):** Returns the value associated with the specified key. Returns None if the key is not found (or a default value if specified).
- **keys():** Returns a view of all keys in the dictionary.
- **values():** Returns a view of all values in the dictionary.
- **items():** Returns a view of all key-value pairs (tuples) in the dictionary.
update(dictionary): Updates the dictionary with key-value pairs from another dictionary.
- **pop(key):** Removes the specified key and its associated value from the dictionary. Returns the value of the removed key.

### Lambda Functions
#### Definition: 
Lambda functions, also known as anonymous functions, are small, anonymous functions defined using the lambda keyword. They can have any number of parameters but can only have one expression.
#### Syntax and example
```
lambda arguments: expression

square = lambda x: x ** 2
print(square(5)) 
# Output: 25
```
### Map and Filter Functions
#### Map: 
Applies a given function to each item of an iterable and returns a list of the results.

#### Syntax and example: 
```
map(function, iterable)

nums = [1, 2, 3, 4, 5]
squared_nums = map(lambda x: x ** 2, nums)
print(list(squared_nums))  # Output: [1, 4, 9, 16, 25]
```

#### Filter: 
Applies a given function to each item of an iterable and returns a list of items for which the function returns True.

#### Syntax and example: 
```
filter(function, iterable)

nums = [1, 2, 3, 4, 5]
even_nums = filter(lambda x: x % 2 == 0, nums)
print(list(even_nums))  # Output: [2, 4]
```

### Exercise 0: Squared Simple
The function `square_matrix_simple` computes the square value of all integers of a matrix. It takes a 2-dimensional array matrix as input and returns a new matrix where each value is the square of the corresponding value in the input matrix.

#### Example:
```
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
# Output: [[1, 4, 9], [16, 25, 36], [49, 64, 81]]

print(matrix)
# Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
In this example, the input matrix is squared element-wise to produce the new matrix.

### Exercise 1: Search and replace
The function `search_replace(my_list, search, replace)` replaces all occurrences of a specified element with another element in a new list.
It returns a new list where all occurrences of the search element are replaced with the replace element.

#### Example:
```
my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)
print(new_list)
# Output: [1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]

print(my_list)
# Output: [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
```
In this example, all occurrences of 2 are replaced with 89 in the list.

### Exercise 2: Unique Addition
The `uniq_add` function takes a list my_list and returns the sum of unique elements in the list. It achieves this by converting the list into a set to remove duplicates, then calculates the sum of the unique elements.

#### Example:
```
my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result:", result)
# Output: Result: 15
```
In this example, the unique elements in the list [1, 2, 3, 1, 4, 2, 5] are [1, 2, 3, 4, 5], and their sum is 15

### Exercise 3: Present in both
The `common_elements` function takes two sets set_1 and set_2 and returns a set containing common elements present in both sets.

#### Example:
```
set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
# Output: ['C']
```
In this example, the common element between set_1 and set_2 is 'C'

### Exercise 4: Only Differents
The function `only_diff_elements` takes two sets set_1 and set_2 and returns a set containing elements that are present in only one of the sets.
It iterates through each element in set_1, if an element is not present in set_2, add it to the diff_set.
Then it iterates again through each element in set_2, if an element is not present in set_1, add it to the diff_set.

#### Example:
```
set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))
# Output: ['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
```
In this example, the elements present only in one of the sets are returned.

### Exercise 5: Number of Keys
The function `number_keys` returns the number of keys in a dictionary. The length of the dictionary is return, which corresponds to the number of keys.

#### Example:
```
a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))
# Output: Number of keys: 3
```
In this example, the number of keys in the dictionary is printed.

### Exercise 6: Print Sorted Dictionary
The function `print_sorted_dictionary` prints a dictionary by ordered keys, sorted in alphabetical order.
It gets the keys of the dictionary, convert them into a list, and sort them in alphabetical order, then iterates through the sorted keys and print each key-value pair.

#### Example:
```
a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)
# Output:
Number: 89
ids: [1, 2, 3]
language: C
track: Low level
```

### Exercise 7: Update Dictionary
The function `update_dictionary` replaces or adds key/value pairs in a dictionary.
If the key exists in the dictionary, its value is replaced with the new value.
If the key does not exist, a new key-value pair is added to the dictionary.

```
a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

# Output:
language: Python
number: 89
track: Low level
--
language: Python
number: 89
track: Low level

```
### Exercise 8: Simple delete by Key
The function `simple_delete` deletes a key from a dictionary.
If the key exists in the dictionary, it is deleted.
If the key does not exist, the dictionary remains unchanged.

#### Example:
```
a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
new_dict = simple_delete(a_dictionary, 'track')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

# Output:
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
```
### Exercise 9: Multiply by 2
The function `multiply_by_2` returns a new dictionary with all values multiplied by 2.
Iterates through each key in the dictionary and multiply its corresponding value by 2.

#### Example:
```
a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

# Output:
Alex: 8
Bob: 14
John: 12
Mike: 14
Molly: 16
--
Alex: 16
Bob: 28
John: 24
Mike: 28
Molly: 32
```

### Exercise 10: Best score
The function `best_score` returns the key with the highest integer value in a dictionary.
If the dictionary is not empty, it finds the key with the maximum value using the max function and returns it.
If the dictionary is empty, returns None.

#### Example:
```
a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

# Output:
Best score: Molly
```

### Exercise 11: Multiply by using Map
The function `multiply_list_map` returns a new list with all values multiplied by a number using map.
It uses map to apply a lambda function that multiplies each element by the specified number to all elements in the list.

#### Example:
```
my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)

# Output:
[4, 8, 12, 16, 24]
[1, 2, 3, 4, 6]
```
