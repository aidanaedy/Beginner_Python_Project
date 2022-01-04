def list_uniqueness(l):

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
    list = [l]
    print(list)
    list_length = {len(l)}

    print(f"List = ", list)
    # converting our list to set
    new_set = set(l)
    print("No of unique items in the list are:", len(new_set))
    unique_items = len(new_set)
    unique_items = [str(unique_items)]
    print(f"unique_items = ", unique_items)
    print(f"list_length = ", list_length)
    print(f"length = {len(list)}")


    zip_iterator = zip(list_length, unique_items)
    dictionary = dict(zip_iterator)

    print(f"dictionary entries" ,dictionary)

#     dictionary = {list_length: unique_items}
    print(f"dictionary = ", dictionary)


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
    dictionary = list_uniqueness(l)
    print(dictionary['list_length'])
    print(dictionary['unique_items'])
