# Problem Statement
#
# We have a collection of strings, and we want to right justify them. Create a class Justifier that contains a method justify that is given a tuple (string) textIn and returns a tuple (string) containing the same strings, right justified, in the same order as they appear in textIn.
# The returned strings should be padded on the left with space characters so that they are all the same length as the longest string in textIn.
# Definition
#
# Class:
# Justifier
# Method:
# justify
# Parameters:
# tuple (string)
# Returns:
# tuple (string)
# Method signature:
# def justify(self, textIn):

#Gendo90 has submitted the 250-point problem for 162.89 points
#Successful on first try!
class Justifier(object):
    def justify(self, textIn):
        wordlengths = [len(text) for text in textIn]
        longest = max(wordlengths)
        newText = []
        # newText = [("{:>" +str(len(longest)) +"s}").format(text) for text in textIn]
        for text in textIn:
            a = longest
            format_string = "{:>" +str(a)+"s}"
            newText.append((format_string).format(text))
        return tuple(newText)


test = Justifier()

print(test.justify(("LONGEST","A","LONGER","SHORT")))
