#! /usr/bin/python3
import sys
import re

sys.version_info[0]

lab_exercise = "Dictionaries"
lab_type = "solution-code"
python_version = ("%s.%s.%s" % (sys.version_info[0], sys.version_info[1], sys.version_info[2]))
print("Exercise: %s" % (lab_exercise))
print("Type: %s" % (lab_type))
print("Python: %s\n" % (python_version))

# ====================================

# CODE1: Create an empty DICTIONARY
dict1 = {}
print("CODE1:")
print(f"dict1 = {dict1}")
print(f"data type = {type(dict1)}")
print(f"length = {len(dict1)}")
print()

# CODE2: Create DICTIONARY with 1 key-value pair
dict2 = {"name": "cloudacademy"}
print("CODE2:")
print(f"dict2 = {dict2}")
print(f"data type = {type(dict2)}")
print(f"length = {len(dict2)}")
print()

# CODE3: Create DICTIONARY with multiple key-value pairs
dict3 = {"name": "cloudacademy", "color": "red", "count": 1000}
print("CODE3:")
print(f"dict3 = {dict3}")
print(f"data type = {type(dict3)}")
print(f"length = {len(dict3)}")
print()

# CODE4: Create DICTIONARY with multiple and nested key-value pairs
dict4 = {"name": "cloudacademy", "color": "red", "count": 1000, "data": {"val1": 1, "val2": 2}}
print("CODE4:")
print(f"set4 = {dict4}")
print(f"data type = {type(dict4)}")
print(f"length = {len(dict4)}")
print()

# CODE5: Iterate over DICTIONARY with multiple and nested key-value pairs
print("CODE5:")
for key, value in dict4.items():
    print(f"key={key}, value={value}")
print()

# CODE6: Search key in DICTIONARY
print("CODE6:")
print("name" in dict4)
print("cloudacademy" in dict4)
print()

# CODE7: Retrieve value from DICTIONARY by key
print("CODE7:")
item0 = dict4["name"]
item1 = dict4["color"]
print(f"item0 = {item0}")
print(f"item1 = {item1}")
print()

# CODE8: Change existing value in DICTIONARY
print("CODE8:")
dict4["name"] = "blah"
dict4["color"] = "blue"
print(f"dict4 = {dict4}")
print(f"data type = {type(dict4)}")
print(f"length = {len(dict4)}")
print()

# CODE9: Add new key-value pair to DICTIONARY
print("CODE8:")
dict4['qwerty'] = 'fast'
print(f"dict4 = {dict4}")
print(f"data type = {type(dict4)}")
print(f"length = {len(dict4)}")
print()

# CODE10: Pop existing key-value pair from DICTIONARY
print("CODE10:")
test = dict4.pop('qwerty', None)
print(f"test = {test}")
print(f"dict4 = {dict4}")
print(f"data type = {type(dict4)}")
print(f"length = {len(dict4)}")
print()

# CODE11: Pop non-existing key-value pair from DICTIONARY
print("CODE11:")
test = dict4.pop('cat', None)
print(f"test = {test}")
print(f"dict4 = {dict4}")
print(f"data type = {type(dict4)}")
print(f"length = {len(dict4)}")
print()

# Test Challenge
print("Test_Challenge:")
dict3 = {"name": "cloudacademy", "count": 1000}
print(f"length = {len(dict3)}")
# unique_items
# print(f"unique_items = {unichr(dict3)}")
print()

# CODE3: Create DICTIONARY with multiple key-value pairs


print("Test_Challenge:")
dict3 = {"name": "Peter", "name2": "Peter"}
list_length = dict3.keys()
print(list_length)
print(f"length = {len(dict3)}")
# print(f"unique_items = {dict.values(dict3)}")
unique = list(set(dict.values(dict3)))
# print(f"unique_items 2 = ", unique)
item_count = len(unique)
print(f"unique_items = ", item_count)
print()

for key, value in dict3.items():
    print(f"key={key}, value={value}")
print()
print(f"unique_items = ", item_count)
print()
print()

print("Start of the List_uniqueness function")
def list_uniqueness(name):
    name = {}
    '''
    Return a dictionary with two key-value pairs:
      1. The key 'list_length' stores the length of the_list as its value.
      2. The key 'unique_items' stores the number of unique items in the_list as its value.
    Arguments
    the_list: A list
    Examples
    l = [1, 2, 2, 4]
    dictionary = list_uniqueness(l)
    print(dictionary['list_length']) # prints 4
    print(dictionary['unique_items']) # prints 3
    '''

    # ====================================
    # Do not change the code before this

    # CODE1: Write code that will create the required dictionary
    
        # list_uniqueness is the function that this is in and the_list is the parameter that is passed
    l = [1, 2, 2, 4]
    list = ["Monday", "Tuesday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    print(list)
    list_length = list

    list_b = ["a", "b", "c", "d", "e", "f"]
    print(list_b)
    unique_items = list_b
    print(f"unique_items = ", unique_items)
    print(f"list_length = ", list_length)
    dictionary = {list_length: unique_items}

    print(list_b)


    '''
    print("the_list values")
    the_list = {"a": "Monday", "b": "Tuesday", "c": "Tuesday", "d": "Wednesday", "e": "Thursday", "f": "Friday"}
    for key, value in the_list.items():
        print(f"key={key}, value={value}")


    list_length = {len(the_list)}
    print(f"length =", list_length)

#     unique = list(set(dict.values(the_list)))
#     one_off = len(unique)

    one_off = list(set(val for dic in unique for val in dic.values()))
    # printing result
    print(f"The original list :", one_off)
#    print(f"The unique values in list are : " + str(one_off))

    dictionary = {the_list: list_length, one_off: unique_items}
    # dictionary = {"list_length": "unique_items"}
    # ex_dict = {"a": "anteater", "b": "bumblebee", "c": "cheetah"}
    '''


    # ====================================
    # Do not change the code after this

    return dictionary

if __name__ == '__main__':
    l = [1, 2, 2, 4]
    dictionary = list_uniqueness(name)
    print(dictionary['list_length'])
    print(dictionary['unique_items'])


# the_list: = "Monday", "Tuesday", "Tuesday", "Wednesday", "Thursday", "Friday"


# list_length = dictionary.keys()
# print(f"length = {len(dict3)}")

# set 2 celled "unique_items"

#  copy to dictionary

