# Problem Statement
#
# Spelling in the English language doesn't make sense. Congress has enacted a plan for orthographical reform (loosely based on Mark Twain's plan for the improvement of English spelling) which will change the spelling of words in the English language gradually over the next 7 years. The plan is as follows:  Year 1:
# - If a word starts with "x", replace the "x" with a "z".
# - Change all remaining "x"s to "ks"s.
# Year 2:
# - Change all "y"s to "i"s.
# Year 3:
# - If a "c" is directly followed by an "e" or "i", change the "c" to an "s".
# Year 4:
# - If a "c" is directly followed by a "k", remove the "c". Keep applying this rule as necessary (Example: "cck" becomes "k".)
# Year 5:
# - If a word starts with "sch", change the "sch" to a "sk".
# - If a "ch" is directly followed by an "r", change the "ch" to a "k".
# - After applying the above rules, change all "c"s that are not directly followed by an "h", to a "k". (This includes all "c"s that are the last letter of a word.)
# Year 6:
# - If a word starts with "kn" change the "kn" to an "n".
# Year 7:
# - Change all double consonants of the same letter to a single consonant. A consonant is any letter that is not one of "a, e, i, o, u." (Example: "apple" becomes "aple"). Keep applying this rule as necessary (Example: "zzz" becomes "z".)
#  The plan requires that rules for each year are followed in the order they are presented, and changes for each year occur after all the changes from previous years.  Write a class Twain, which contains a method getNewSpelling. getNewSpelling takes as parameters an integer year representing the number of years that have passed since the plan to improve the English language began, and a string phrase representing the English phrase to convert. For the purposes of the plan, a word is a sequence of lowercase letters ('a'-'z') bounded by spaces or the start/end of phrase. The method returns a string representing the converted phrase.
# Definition
#
# Class:
# Twain
# Method:
# getNewSpelling
# Parameters:
# integer, string
# Returns:
# string
# Method signature:
# def getNewSpelling(self, year, phrase):

# Gendo90 has submitted the 500-point problem for 150.00 points
# Successful on second try!
# Missed the "sys.maxsize" optional parameter for the "replace()" call for
# kn
# Probably would make sense to skip this problem if actually encountered in
# a competition...
import string

class Twain(object):
    def yearOne(self, words):
        newWords = []
        for word in words:
            word = [a for a in word]
            if(word[0]=="x"):
                word[0]="z"
            word = word[0] + "".join("ks" if (a=="x") else a for a in word[1:])
            newWords.append(word)
        words = " ".join(newWords)
        return words

    def yearTwo(self, words):
        newWords = []
        words = words.split(" ")
        for word in words:
            word = ["i" if (a=="y") else a for a in word]
            word = "".join(a for a in word)
            newWords.append(word)
        words = " ".join(newWords)
        return words

    def yearThree(self, words):
        newWords = []
        words = words.split(" ")
        for word in words:
            this_word = [a for a in word]
            for i, letter in enumerate(word):
                if(letter=="c"):
                    if(i+1<len(word) and (word[i+1]=="e" or word[i+1]=="i")):
                        this_word[i] = "s"
            this_word = "".join(a for a in this_word)
            newWords.append(this_word)
        words = " ".join(newWords)
        return words

    def yearFour(self, words):
        newWords = []
        words = words.split(" ")
        for word in words:
            this_word = [a for a in word]
            i = len(this_word)-1
            while(i>0):
                if(this_word[i]=="k"):
                    if(i-1>=0 and (this_word[i-1]=="c")):
                        this_word.pop(i-1)
                i-=1
            this_word = "".join(a for a in this_word)
            newWords.append(this_word)
        words = " ".join(newWords)
        return words

    def yearFive(self, words):
        words = words.split(" ")
        newWords = []
        for word in words:
            if(word[0:3]=="sch"):
                this_word = word.replace("sch", "sk")
            else:
                this_word = word
            while("chr" in this_word):
                spot = this_word.find("chr")
                l = [a for a in this_word]
                l[spot] = "k"
                l.pop(spot+1)
                this_word = "".join(a for a in l)
            l = [a for a in this_word]
            for i, letter in enumerate(l):
                if(letter=="c"):
                    if(i==len(l)-1):
                        l[i] = "k"
                    elif(i+1<len(l) and l[i+1]!="h"):
                        l[i] = "k"
            this_word = "".join(a for a in l)
            newWords.append(this_word)
        words = " ".join(newWords)
        return words

    def yearSix(self, words):
        words = words.split(" ")
        newWords = []
        for word in words:
            if(word[0:2]=="kn"):
                this_word = word.replace("kn", "n", 1)
            else:
                this_word = word
            newWords.append(this_word)
        words = " ".join(newWords)
        return words

    def yearSeven(self, words):
        words = words.split(" ")
        vowels = {'a':True, 'e':True, 'i':True, 'o':True, 'u': True}
        newWords = []
        for word in words:
            this_word = [a for a in word]
            i = 0
            while(i<len(this_word)):
                if(i+1<len(this_word)):
                    if(this_word[i]==this_word[i+1] and this_word[i] not in vowels):
                        this_word.pop(i+1)
                        i-=1
                i+=1
            this_word = "".join(a for a in this_word)
            newWords.append(this_word)
        words = " ".join(newWords)
        return words


    def getNewSpelling(self, year, phrase):
        # words = phrase.split(" ")
        whitespaces = []
        words = [""]
        for i, letter in enumerate(phrase):
            if(letter==" "):
                whitespaces.append(True)
            else:
                words[-1]+=letter
                whitespaces.append(False)
            if(letter!=" " and i+1<len(phrase)):
                if(phrase[i+1]==" "):
                    words.append("")
        if(words[-1]==""):
            words.pop()
        if(not words):
            return ""
        if(year==0):
            return phrase
        if(year==1):
            words = (self.yearOne(words))
        if(year==2):
            words = self.yearOne(words)
            words = self.yearTwo(words)
        if(year==3):
            words = self.yearOne(words)
            words = self.yearTwo(words)
            words = self.yearThree(words)
        if(year==4):
            words = self.yearOne(words)
            words = self.yearTwo(words)
            words = self.yearThree(words)
            words = self.yearFour(words)
        if(year==5):
            words = self.yearOne(words)
            words = self.yearTwo(words)
            words = self.yearThree(words)
            words = self.yearFour(words)
            words = self.yearFive(words)
        if(year==6):
            words = self.yearOne(words)
            words = self.yearTwo(words)
            words = self.yearThree(words)
            words = self.yearFour(words)
            words = self.yearFive(words)
            words = self.yearSix(words)
        if(year==7):
            words = self.yearOne(words)
            words = self.yearTwo(words)
            words = self.yearThree(words)
            words = self.yearFour(words)
            words = self.yearFive(words)
            words = self.yearSix(words)
            words = self.yearSeven(words)

        output = ""
        i = 0
        words = words.split(" ")
        if(whitespaces):
            last = whitespaces[0]
        else:
            last = True
        if(last==False):
            output+=words.pop(0)
        while(whitespaces):
            if(whitespaces[0]==True):
                output+=" "
            if(last==True and whitespaces[0] is False):
                output+=words.pop(0)

            last = whitespaces.pop(0)

        while(words):
            output+=words.pop(0)

        return output


test = Twain()

print(test.getNewSpelling(7, "thsks zst sik tes ofk nkn zoop zoks sisi"))
