# Problem Statement
#
# There exists a basic encryption method known as ROT13. One property of ROT13 is that the encryption and decryption processes are exactly the same. These processes work by doing a simple transformation from one letter of the alphabet to another. The letters A through M become N through Z, such that A->N, B->O, ..., M->Z. The letters N through Z become A through M, such that N->A, O->B, ..., Z->M.  One of the problems with most implementations is that everything is converted to upper case. Another problem is that numbers are ignored completely, leaving them unencrypted. One way to overcome these limitations is to extend ROT13 to cover lowercase letters as well as numbers. Here is how our extended ROT transformations will work:
# characters   become
#    A-M        N-Z
#    N-Z        A-M
#    a-m        n-z
#    n-z        a-m
#    0-4        5-9
#    5-9        0-4
#  For example, the message "Uryyb 28" would become "Hello 73" after being transformed.
#    U -> H        2 -> 7
#    r -> e        8 -> 3
#    y -> l
#    y -> l
#    b -> 0
# Notice that the spaces were left as is.  You have intercepted a message which you believe to be encrypted using this process. Create a class SuperRot with a method decoder that takes a string message and returns the decoded message as a string.
# Definition
#
# Class:
# SuperRot
# Method:
# decoder
# Parameters:
# string
# Returns:
# string
# Method signature:
# def decoder(self, message):

import string
# Gendo90 has submitted the 450-point problem for 360.65 points
# Successful on first try!
class SuperRot(object):
    def decoder(self, message):
        uppercaseLetters = [a for a in string.ascii_uppercase]
        lowercaseLetters = [a for a in string.ascii_lowercase]
        nums = [a for a in range(10)]
        output = ""

        for item in message:
            try:
                this_num = int(item)
                std_index = nums.index(this_num)
                if(std_index<=4):
                    output+=str(nums[std_index+5])
                else:
                    output+=str(nums[std_index-5])
            except ValueError:
                if(item in uppercaseLetters):
                    std_index = uppercaseLetters.index(item)
                    if(std_index<=12):
                        output+=uppercaseLetters[std_index+13]
                    else:
                        output+=uppercaseLetters[std_index-13]
                elif(item in lowercaseLetters):
                    std_index = lowercaseLetters.index(item)
                    if(std_index<=12):
                        output+=lowercaseLetters[std_index+13]
                    else:
                        output+=lowercaseLetters[std_index-13]
                else:
                    output+=item

        return output


test = SuperRot()

print(test.decoder("Uryyb 28"))
