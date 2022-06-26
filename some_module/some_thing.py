""" Simple module to practice writing tests against """


import sys


def do_some_thing(param):
    """ cast to int before return if possible """
    print ("some_thing happened:", param)
    try:
        param = int(param)
    except ValueError:
        pass
    return param


def do_some_other_thing(param):
    """ cast to int and add 1 before return if possible, or just add 1 to string """
    print ("some_other_thing happened:", param)
    try:
        param = int(param)
        param +=1
    except ValueError:
        param = param + "1"
    return param


def do_every_thing(param1, param2):
    """
    orchestrating function - makes use of other functions in the module
    if you pass 2 ints, they will be processed by other functions, added and returned as int
    if you pass 2 values not castable as ints, a combined string will be returned
    if you pass 1 value that is an int and one that isn't, it will raise a ValueError
    """
    some_thing = do_some_thing(param1)
    some_other_thing = do_some_other_thing(param2)
    result = None
    try:
        result = some_thing + some_other_thing
        print("every_thing came together:", result)
    except TypeError as exc:
        raise ValueError("incompatible types - please pass same type for each param") from exc
    return result


if __name__ == '__main__':
    do_every_thing(sys.argv[1], sys.argv[2])
