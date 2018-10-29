# Write a Python program to calculate the length of a string


def length_of_string(str_in):
    length = 0
    for character in str_in:
        length += 1
    return length


# Write a Python program to get a string made of the first 2 and the last 2 chars
# from a given a string. If the string length is less than 2, return None.

# Sample String : 'helloworld'
# Expected Result : 'held'
# Sample String : 'he'
# Expected Result : 'hehe'
# Sample String : 'h'
# Expected Result : None


def first_last(str_in):
    if len(str_in) >= 2:
        first = str_in[0] + str_in[1]
        last = str_in[len(str_in) - 2] + str_in[len(str_in) - 1]
        return first + last
    else:
        return None


# Write a Python program to sum all the items in a list and return the value.


def sum(list_in):
    add = 0
    for items in list_in:
        add += items
    return add


# Write a Python program to count the number of strings where the string length is 2
# or more and the first and last character are same from a given list of strings.

# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2


def num_strings(list_in):
    num = 0
    for item in list_in:
        if len(item) >= 2 and str(item[0]) == str(item[len(item) - 1]):
            num += 1
    return num


# Write a function to check if a given key already exists in a dictionary.
# Return true if the key exists, false otherwise.


def key_exists(dict_in, key_in):
    if key_in in dict_in:
        return True
    else:
        return False


# call functions below
print(length_of_string("Hello, World!"))
print(length_of_string(""))
print(length_of_string("A"))

print(first_last("helloworld"))
print(first_last("he"))
print(first_last("h"))

print(sum([1, 3, 5, 2, 6]))
print(sum([]))
print(sum([5]))

print(num_strings(['abc', 'xyz', 'aba', '1221']))
print(num_strings([]))
print(["abc"])

my_dict = {"hello": 1, "world": 2, "code": 3, "connects": 5}
print(key_exists(my_dict, "code"))
print(key_exists(my_dict, "2018"))
