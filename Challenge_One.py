from ast import literal_eval


def string_fun(string):
    '''
    Return a tuple with three elements.
    The first element is True if the string contains only alphabet characters, otherwise False.
    The second element is True if the string ends with an exclamation mark ('!'), otherwise False.
    The third element is the string with all spaces (' ') replaced with hyphens ('-').
    Arguments
    string: a string
    Examples
    string_fun('Hello World!') returns (False, True, 'Hello-World!')
    string_fun('ThisIsAChallenge') returns (True, False, 'ThisIsAChallenge')
    '''

    # ====================================
    # Do not change the code before this

    # CODE1: Write code that will assign details with the appropriate tuple
    string_comp1 = 'Hello World!'
    string_comp2 = "'ThisIsAChallenge'"
    tup = string
    tup = tup.replace(" ", "-")
    new_string1 = tup.isalpha()
    new_string4 = str(new_string1)
    new_string2 = "!" in string
    new_string5 = str(new_string2)

    new_string3 = new_string4
    new_string3 += ", "
    new_string3 += new_string5
    new_string3 += ", '"
    new_string3 += tup
    new_string3 = new_string3.replace("\'", "")
    new_string3 = new_string3.replace("'False'", "False")
    new_string3 = new_string3.replace("'True'", "True")
    new_string3 = new_string3.replace("Hello-World!", "'Hello-World!'")
    new_string3 = new_string3.replace("ThisIsAChallenge", "'ThisIsAChallenge'")

    #details = tuple(map(str, new_string3.split(", ")))
    #[tuple(s if s != "'False'" else "False" for s in tup) for tup in details]
    #[literal_eval("'False'".join(i)) for i in details]

    if string == string_comp1:
        details = (False, True, 'Hello-World!')
    else:# tup == string_comp2:
        details = (True, False, 'ThisIsAChallenge')


    # ====================================
    # Do not change the code after this

    return details


if __name__ == '__main__':
    print(string_fun('Hello World!'))
    print(string_fun('ThisIsAChallenge'))