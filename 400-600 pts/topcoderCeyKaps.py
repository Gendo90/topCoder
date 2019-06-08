import string
# Problem Statement
#
# The keycaps on a keyboard have been switched around, and the user is now trying to remember what he was trying to type.
# Create a class CeyKaps containing the method decipher that takes a string typed, representing the visible message on the screen, and a tuple (string) switched, representing the keycap switches. The method should return the original intended message (what keys the user thought he was pressing).
# A keycap can be switched around more than once. For example, if someone switched around 'A' and 'S', then switched around 'S' and 'D', then 'D' would be where 'A' originally was, 'S' where 'D' was, and 'A' where 'S' was.
# The elements of switches will be formatted as (quotes added for clarity) "*:*", where the *'s represent the keycaps to be switched. The above example would be represented as: {"A:S","S:D","D:A"}, or alternately as {"S:A","D:S","A:D"} or any other such combination. The order of the keycaps doesn't matter, but the order of the switches does.
# Definition
#
# Class:
# CeyKaps
# Method:
# decipher
# Parameters:
# string, tuple (string)
# Returns:
# string
# Method signature:
# def decipher(self, typed, switches):

# Gendo90 has submitted the 600-point problem for 417.24 points
# Successful on first try!
class CeyKaps(object):
    def decipher(self, typed, switches):
        keyboard_state = [ord(letter) for letter in string.ascii_uppercase]
        output_message = ""
        for item in switches:
            first_letter = ord(item[0])
            second_letter = ord(item[2])
            first_ind = keyboard_state.index(first_letter)
            second_ind = keyboard_state.index(second_letter)
            keyboard_state[first_ind], keyboard_state[second_ind] = keyboard_state[second_ind], keyboard_state[first_ind]
        for letter in typed:
            actual_letter = string.ascii_uppercase.index(letter)
            output_message+=chr(keyboard_state[actual_letter])

        return output_message


test = CeyKaps()

print(test.decipher("AAAAA", ("A:B","B:C","A:D")))
