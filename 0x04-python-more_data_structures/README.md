# READ ME
1. 0-square_matrix_simple.py: A function that computes the square value of all integers of a matrix.

    Prototype: def square_matrix_simple(matrix=[]):
    matrix is a 2 dimensional array
    Returns a new matrix:
        Same size as matrix
        Each value should be the square of the value of the input
    Initial matrix should not be modified
    You are not allowed to import any module
    You are allowed to use regular loops, map, etc

2. 1-search_replace.py: a function that replaces all occurrences of an element by another in a new list.

    Prototype: def search_replace(my_list, search, replace):
    my_list is the initial list
    search is the element to replace in the list
    replace is the new element
    You are not allowed to import any module

3. 2-uniq_add.py: a function that replaces all occurrences of an element by another in a new list.

    Prototype: def search_replace(my_list, search, replace):
    my_list is the initial list
    search is the element to replace in the list
    replace is the new element
    You are not allowed to import any module

4.  5-number_keys.py: a function that returns the number of keys in a dictionary.
<pre><code>guillaume@ubuntu:~/0x04$ cat 5-main.py
#!/usr/bin/python3
number_keys = __import__('5-number_keys').number_keys

a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))

guillaume@ubuntu:~/0x04$ ./5-main.py
Number of keys: 3
guillaume@ubuntu:~/0x04$
</pre></code>

5. 6-print_sorted_dictionary.py: a function that prints a dictionary by ordered keys.

    Prototype: def print_sorted_dictionary(a_dictionary):
    You can assume that all keys are strings
    Keys should be sorted by alphabetic order
    Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
    Dictionary values can have any type
    You are not allowed to import any module

6. 7-update_dictionary.py: a function that replaces or adds key/value in a dictionary.

    Prototype: def update_dictionary(a_dictionary, key, value):
    key argument will be always a string
    value argument will be any type
    If a key exists in the dictionary, the value will be replaced
    If a key doesn’t exist in the dictionary, it will be created
    You are not allowed to import any module

7. 8-simple_delete.py: a function that deletes a key in a dictionary.

    Prototype: def simple_delete(a_dictionary, key=""):
    key argument will be always a string
    If a key doesn’t exist, the dictionary won’t change
    You are not allowed to import any module

8. 9-multiply_by_2.py: a function that returns a new dictionary with all values multiplied by 2

    Prototype: def multiply_by_2(a_dictionary):
    You can assume that all values are only integers
    Returns a new dictionary
    You are not allowed to import any module


10.  
