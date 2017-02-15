def main():
    # Welcome to Dictionary {}
    print(3*'*', 'Welcome To Dictionary {}', 3*'*')

    # to Create a Dict:
    print('\n$ Create a Dict')
    dict1 = {'name': 'Omar', 'age': 17}
    print(dict1, type(dict1))

    # To show a key:
    print('\n$ Show key')
    print(dict1['name'])

    # To add a new value:
    print('\n$ add an new value')
    dict1['jop'] = 'Student'
    print(dict1)

    # To delete a value:
    print('\n$ delete a value')
    del dict1['jop']
    print(dict1)

    # dict method

    # 1- clear(), The method clear() removes all items from the dictionary.
    # This method doesn't return any value.
    # Syntax => dict.clear()
    dict1 = {'name': 'Omar', 'age': 17}
    dict1.clear()
    print('\n$ After use clear()')
    print(dict1)

    # 2- copy(), The method copy() returns a shallow copy of the dictionary.
    # This method returns a shallow copy of the dictionary.
    # Syntax => dict.copy()
    dict1 = {'name': 'Omar', 'age': 17}
    new_dict = dict1.copy()
    print('\n$ new dict, copy from dict1:')
    print(new_dict)

    # 3- get(), The method get() returns a value for the given key.
    # If key is not available then returns default value None.
    # Syntax => dict.get(key)
    dict1 = {'name': 'Omar', 'age': 17}
    print('\n$ get value by keys')
    print(dict1.get('name'))

    # 4- items(), The method items() returns a list of dict's (key, value) tuple pairs
    # Syntax => dict.items()
    dict1 = {'name': 'Omar', 'age': 17}
    print('\n$ print key & value')
    print(dict1.items())

    # 5- keys(), The method keys() returns a list of all the available keys in the dictionary.
    # Syntax => dict.keys()
    dict1 = {'name': 'Omar', 'age': 17}
    print('\n$ print keys only')
    print(dict1.keys())

    # 6- values(), The method values() returns a list of all the values available in a given dictionary.
    # Syntax => dict.values()
    dict1 = {'name': 'Omar', 'age': 17}
    print('\n$ print values only')
    print(dict1.values())

    # 7- update(), The method update() adds dictionary dict2's key-values pairs in to dict.
    #  This function does not return anything.
    # Syntax => dict.update(dict2)
    dict1 = {'name': 'Omar', 'age': 17}
    dict2 = {'jop': 'Student', 'Class': 13}
    print('\n$ add dict2 to dict1')
    dict1.update(dict2)
    print(dict1)

if __name__ == '__main__':
    main()












