# Gendo90 has submitted the 250-point problem for 196.66 points
# Successful on first go! Took ~14 minutes
class CCipher(object):
    def decode(self, cipherText, shift):
        ans = []
        for letter in cipherText:
            this_unicode = ord(letter)
            if (this_unicode-shift)<65:
                this_unicode = this_unicode - shift + 90 - 64
            else:
                this_unicode -= shift
            new_letter = chr(this_unicode)
            ans.append(new_letter)
        return "".join(ans)

test = CCipher()

print(test.decode("VQREQFGT", 2))
