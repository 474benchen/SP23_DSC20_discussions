"""
DSC20 Bootcamp week 1
Name: SOLUTIONS
PID: SOLUTIONS
"""

# Question 1
def check_integer(num):
    """
    A function that returns True if the input parameter is 1, 
    return False if input is 0, otherwise return "I don’t know". 
    ---
    Parameters:
    num: the input parameter to check
    ---
    Return True, False, or “I don’t know" based on the input

    >>> check_integer(1)
    True
    >>> check_integer(0)
    False
    >>> check_integer(10)
    "I don't know"
    """
    if num==1:
        return True
    elif num==0:
        return False
    else:
        return "I don't know"


# Question 2
def check_list(lst):
    """
    A function that returns “find :)" if 0 is in the list, 
    return “I can’t find :(" otherwise. 
    ---
    Parameters:
    lst: the input parameter to check
    ---
    Return “find :)" or “I can’t find :(" based on the input

    >>> check_list([0, 1])
    'find :)'
    >>> check_list([])
    "I can't find :("
    """
    for i in lst:
        if i == 0:
            return "find :)"

    return "I can't find :("


# Question 3
def num_of_treasure(lst):
    """
    A function that calculates how many “treasure" there is in the list. 
    ---
    Parameters:
    lst: the input parameter to check
    ---
    Return the number of “treasure" in the list

    >>> num_of_treasure([0, 1])
    0
    >>> num_of_treasure(['treasure', 'treasure', 0, 1])
    2
    >>> num_of_treasure(['Treasure', 'treasure', 0, 1])
    1
    """
    counter = 0
    for i in lst:
        if i == "treasure":
            counter+=1
    return counter


# Question 4
def add_connection(pos):
    """
    A function that inserts "-" between each number in 
    the range of 0 to the input integer (0 and input 
    integer both inclusive). 
    ---
    Parameters:
    pos: a positive integer which represents the upper bound(inclusive)
    ---
    Return the new string after insertions

    >>> add_connection(1)
    '0-1'
    >>> add_connection(3)
    '0-1-2-3'
    """
    output = list(range(pos+1))
    for i in output:
        output[i] = str(i)
    return '-'.join(output)


# Question 5
def find_ith_element(lst, i):
    """
    A function that takes a list and an integer, finds the i_th element. 
    ---
    Parameters:
    lst: the list with elements to be found
    i: the integer which represents the i_th element to be found
    ---
    Return the i_th element in the list. If i is out of bound, return "Haiya".

    >>> find_ith_element(["R", "D", "L", "C", "J"], 1)
    'R'
    >>> find_ith_element(["R", "D", "L", "C", "J"], 0)
    'Haiya'
    >>> find_ith_element(["R", "D", "L", "C", "J"], 5)
    'J'
    """
    if i > len(lst) or i<1:
        return "Haiya"
    return lst[i-1]


# Question 6
def head_tail_compare(lst):
    """
    A function that compares the first element and the last element in the 
    input list.
    ---
    Parameters:
    lst: a list of numbers
    ---
    Print True if they are the same, False if not
    Return the larger element

    >>> input1 = [1, 2, 3, 4, 5]
    >>> input2 = [2, 2]
    >>> head_tail_compare(input1)
    False
    5
    >>> head_tail_compare(input2)
    True
    2
    """
    print (lst[0] == lst[len(lst)-1])
    return max(lst[0], lst[len(lst)-1])


# Question 7
def compare_string_length(string, i):
    """
    A function that compares the length of a string to an integer
    ---
    Parameters:
    String: a string
    i: an integer
    ---
    Return True if str has a length greater than i, False if not
    >>> trial = 'DSC20'
    >>> i = 10
    >>> compare_string_length(trial, i)
    False
    >>> j = 1
    >>> compare_string_length(trial, j)
    True
    """
    return len(string) > i


# Question 8
def is_even(number):
    """
    Determine whether the input is even.
    ---
    Parameters:
    number: an integer
    ---
    Return True if the integer is even, otherwise False
    
    >>> is_even(6)
    True
    >>> is_even(111)
    False
    """
    return number%2==0


# Question 9
def round_float(number):
    """
    A function to round a float into its closest integer form.
    ---
    Parameters:
    number: a float value
    ---
    Return the closest integer form of number.
    
    >>> round_float(7.0)
    7
    >>> round_float(111.45)
    111
    >>> round_float(68.7)
    69
    """
    return round(number)


# Question 10
def round_list(lst):
    """
    A function to round all values within a list into its 
    closest integer form.
    ---
    Parameters:
    lst: a list of numeric values
    ---
    Return a list containing rounded integers.
    
    >>> round_list([6.9, 4.2, 3.3, 4.0])
    [7, 4, 3, 4]
    >>> round_list([33.3, 114.55, 46.21])
    [33, 115, 46]
    >>> round_list([16.115, 40.9, 70.75, 9.99, 1.5])
    [16, 41, 71, 10, 2]
    """
    output = []
    for i in lst:
        output.append(round(i))

    return output

# Question 11
def take_first(lst):
    """
    A function to take the first letter of each string in the list 
    and combine it to a string.
    ---
    Parameters:
    lst: a list of strings
    ---
    Return a string.
    
    >>> take_first(['ab','cd','ef'])
    'ace'
    >>> take_first(['ma','aa','ra','ia','na','aa'])
    'marina'
    >>> take_first(['12',''])
    '1'
    """
    output = ''
    for i in lst:
        if len(i) > 0:
            output+=i[0]
    return output


# Question 12
def factorial(number):
    """
    A function to return the factorial of the given number
    ---
    Parameters:
    number: a positive integer
    ---
    Returns an integer
    
    >>> factorial(3)
    6
    >>> factorial(1)
    1
    >>> factorial(8)
    40320
    """
    out = 1
    while number > 0:
        out*=number
        number-=1
    return out


# Question 13
def convert_string(word, number):
    """
    A function to return the number based on whether or not word 
    contains certain characters.
    ---
    Parameters:
    Word: a string
    number: a positive integer
    ---
    Returns an integer
    
    >>> convert_string("dsc30", 2)
    100
    >>> convert_string("dsc20", 100)
    200
    >>> convert_string("dosidos", 10)
    230
    """
    out = number

    for char in word:
        if char == '2':
            out+=2
        elif char == '0':
            out-=2
        elif char == 'd':
            out+=60
        elif char == 's':
            out+=50
        elif char == 'c':
            out-=10
        else:
            pass

    return out


