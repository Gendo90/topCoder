#Problem Statement
#    
#A prefix code is a set of words in which no word is a prefix of another word in the set. A word v is said to be a prefix of a word w if w starts with v.  An important property of prefix codes is that they are uniquely decodable. Prefix codes are commonly used - telephone numbers are an everyday example (as you probably don't want a stranger to pick up the phone call you make just because his number is a prefix of the number you intend to dial). Prefix codes are also very popular in computer #science, the Huffman code used for data compression being a famous example.  Given a tuple (string) words, return the string "Yes" if that set of words is a prefix code or return the string "No, i" if it is not, where i is replaced by the lowest 0-based index of a string in words that is a prefix of another string in words. (That index should have no extra leading zeros.)
#Definition
#    
#Class:
#PrefixCode
#Method:
#isOne
#Parameters:
#tuple (string)
#Returns:
#string
#Method signature:
#def isOne(self, words):

#Gendo90 has submitted the 250-point problem for 177.59 points

#Successful on first try!
class PrefixCode(object):
    def isOne(self, words):
        if len(words)==1:
            return "Yes"

        for i, item in enumerate(words):
            z = [x.find(item) if x!=item else item for x in words]
            print(z)
            if 0 in z:
                loc = z.index(item)
                return "No, "+str(loc)

        return "Yes"

test = PrefixCode()

print(test.isOne(["not", "no"]))
