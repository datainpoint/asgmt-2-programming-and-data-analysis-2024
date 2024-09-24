# asgmt-2-programming-and-data-analysis-2024

> Assignment 2: Programming and Data Analysis 2024.

- Define functions in `asgmt.py` given their names, templates, and docstrings.
- Run `test-runner.py` to validate your functions.
- Upload `asgmt.py` to [NTU COOL](https://cool.ntu.edu.tw).

## 01. Define a function `convert_integer_to_weekday()` which converts given integer to weekday names.

```python
def convert_integer_to_weekday(x: int) -> str:
    """
    >>> convert_integer_to_weekday(0)
    "Sunday"
    >>> convert_integer_to_weekday(1)
    "Monday"
    >>> convert_integer_to_weekday(2)
    "Tuesday"
    >>> convert_integer_to_weekday(3)
    "Wednesday"
    >>> convert_integer_to_weekday(4)
    "Thursday"
    >>> convert_integer_to_weekday(5)
    "Friday"
    >>> convert_integer_to_weekday(6)
    "Saturday"
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 02. Define a function `convert_integer_to_weekday_and_abb()` which converts given integer to weekday names and their abbreviations.

```python
def convert_integer_to_weekday_and_abb(x: int) -> tuple:
    """
    >>> convert_integer_to_weekday_and_abb(0)
    ("Sunday", "Sun")
    >>> convert_integer_to_weekday_and_abb(1)
    ("Monday", "Mon")
    >>> convert_integer_to_weekday_and_abb(2)
    ("Tuesday", "Tue")
    >>> convert_integer_to_weekday_and_abb(3)
    ("Wednesday", "Wed")
    >>> convert_integer_to_weekday_and_abb(4)
    ("Thursday", "Thu")
    >>> convert_integer_to_weekday_and_abb(5)
    ("Friday", "Fri")
    >>> convert_integer_to_weekday_and_abb(6)
    ("Saturday", "Sat")
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 03. Define a function `sort_list_with_ascending_order()` which sorts a given list with ascending order.

```python
def sort_list_with_ascending_order(x: list) -> list:
    """
    >>> sort_list_with_ascending_order([2, 5, 3])
    [2, 3, 5]
    >>> sort_list_with_ascending_order([2, 5, 3, 11, 7])
    [2, 3, 5, 7, 11]
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 04. Define a function `sort_list_with_descending_order()` which sorts a given list with descending order.

```python
def sort_list_with_descending_order(x: list) -> list:
    """
    >>> sort_list_with_descending_order([2, 5, 3])
    [5, 3, 2]
    >>> sort_list_with_descending_order([2, 5, 3, 11, 7])
    [11, 7, 5, 3, 2]
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 05. Define a function `remove_the_first_and_last_element()` which removes the first and the last element given a list whose length is greater than 3.

```python
def remove_the_first_and_last_element(x: list) -> list:
    """
    >>> remove_the_first_and_last_element([2, 3, 5, 7, 11])
    [3, 5, 7]
    >>> remove_the_first_and_last_element(["Python", "Reticulate", "Anaconda"])
    ["Reticulate"]
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 06. Define a function `retrieve_the_first_three_characters()` which retrieves the first three characters given a string.

```python
def retrieve_the_first_three_characters(x: str) -> str:
    """
    >>> retrieve_the_first_three_characters("Python")
    "Pyt"
    >>> retrieve_the_first_three_characters("Reticulate")
    "Ret"
    >>> retrieve_the_first_three_characters("Anaconda")
    "Ana"
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 07. Define a function `convert_weekday_to_integer()` which converts weekday name to integer.

```python
def convert_weekday_to_integer(weekday_name: str) -> int:
    """
    >>> convert_weekday_to_integer("Sunday")
    0
    >>> convert_weekday_to_integer("Monday")
    1
    >>> convert_weekday_to_integer("Tuesday")
    2
    >>> convert_weekday_to_integer("Wednesday")
    3
    >>> convert_weekday_to_integer("Thursday")
    4
    >>> convert_weekday_to_integer("Friday")
    5
    >>> convert_weekday_to_integer("Saturday")
    6
    """
    ### BEGIN SOLUTION

    ### END SOLUTION
```

## 08. Define a function `find_taipei_city_zip_code()` which returns the 3-digit zip code given an area name of Taipei city.

Source: [臺北市行政區劃](https://zh.wikipedia.org/wiki/%E8%87%BA%E5%8C%97%E5%B8%82%E8%A1%8C%E6%94%BF%E5%8D%80%E5%8A%83)

```python
def find_taipei_city_zip_code(area_name: str) -> int:
    """
    >>> find_taipei_city_zip_code("中正區")
    100
    >>> find_taipei_city_zip_code("大同區")
    103
    >>> find_taipei_city_zip_code("中山區")
    104
    """
    ### BEGIN SOLUTION

    ### END SOLUTION
```

## 09. Define a function `sing_do_re_mi()` which returns the lyrics of "Do-Re-Mi".

Source: <https://youtu.be/Qy9cj-zwbVY>

```python
def sing_do_re_mi(note: str) -> str:
    """
    >>> sing_do_re_mi("Do")
    'a deer, a female deer.'
    >>> sing_do_re_mi("Re")
    'a drop of golden sun.'
    >>> sing_do_re_mi("Mi")
    'a name I call myself.'
    >>> sing_do_re_mi("Fa")
    'a long long way to run.'
    >>> sing_do_re_mi("So")
    'a needle pulling thread.'
    >>> sing_do_re_mi("La")
    'a note to follow so.'
    >>> sing_do_re_mi("Ti")
    'a drink with jam and bread.'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 10. Define a function `remove_duplicates()` which removes duplicate elements given a list and returns with ascending order.

```python
def remove_duplicates(x: list) -> list:
    """
    >>> remove_duplicates([5, 5, 6, 6])
    [5, 6]
    >>> remove_duplicates([2, 2, 6, 6])
    [2, 6]
    >>> remove_duplicates([9, 9, 8, 1])
    [1, 8, 9]
    """
    ### BEGIN SOLUTION

    ### END SOLUTION
```