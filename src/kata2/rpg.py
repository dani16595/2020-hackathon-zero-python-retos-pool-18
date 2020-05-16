#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    """
    Generate a passLen-sized password
    :param passLen: integer sized password default 10
    :return: key : string password
    """
    #
    #
    key = ''
    valid_characters_list = string.ascii_letters + string.digits
    for i in range(passLen):
        character = random.choice(valid_characters_list)
        key = key + character
    #
    #
    return key
