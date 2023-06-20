#!/usr/bin/env python3

def validate_user(username, minlen):
    #It is possible to ommit the assertions like this one
    #below by starting script with -O parameter.
    assert type(username) == str, "username must be a string"
    if type(username) != str:
        raise TypeError("wrong data type of username: must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True