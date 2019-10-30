# Problem Statement
#
# Some people like to have a particular custom signature following their emails or posts on online message boards. These signatures usually contain the handle by which they are known, but then are decorated by various punctuation marks to make them look more interesting. You, as administrator of a popular message board, would like to allow such decorations in people's signatures while enforcing a rule that the signature they use contains their name. In order to do this, you allow people to set up a series of rules to apply to their handles to automatically generate their signatures.
# You will be given a user's handle as a string, which will be made up of upper- and lower-case letters, numbers or underscores ('_'). You will also be given two tuple (string)s representing a series of formatting commands. Each element in commands is "prepend", "append" or "surround". Each element of decorations is a series of punctuation characters (out of ,./;'<>?:"\|[]{}-=_+!@#$%^&*()~` ) to use. The ith element of commands corresponds to the ith element of decorations.
# Each instruction should be executed as follows:
# For a "prepend" command, put the decoration at the beginning of the name.
# For an "append" command, put the decoration at the end of the name.
# For a "surround" command, put the decoration at the beginning of the name and backwards at the end of the name.
# The instructions should be executed in the order in which they appear, so if name is "Bob", commands is {"surround", "append", "prepend"}, and decorations is {"-=", "(", ")"} name would progressively go from "Bob" to "-=Bob=-" to "-=Bob=-(" to ")-=Bob=-(".
# Definition
#
# Class:
# SignatureDecorator
# Method:
# applyDecoration
# Parameters:
# string, tuple (string), tuple (string)
# Returns:
# string
# Method signature:
# def applyDecoration(self, name, commands, decorations):


#Gendo90 has submitted the 250-point problem for 221.38 points
#Successful on first try!
#A little tricky to get the mid-1 part (because the array index starts at 0)
class SignatureDecorator(object):
    def applyDecoration(self, name, commands, decorations):
        output = name
        if(not isinstance(commands, tuple)):
            if(commands=="append"):
                output+=decorations
            elif(commands=="prepend"):
                output=decorations+output
            else:
                output = decorations+output+decorations[::-1]
            return output

        for i in range(len(commands)):
            if(commands[i]=="append"):
                output+=decorations[i]
            elif(commands[i]=="prepend"):
                output=decorations[i]+output
            else:
                output = decorations[i]+output+decorations[i][::-1]

        return output



test = SignatureDecorator()

#workaround that is good to know about!
print(test.applyDecoration("Bob", ("append"), ("-")))
# print(test.unscramble(tuple(1), 20))
