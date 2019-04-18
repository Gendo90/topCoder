class BinaryCode(object):
    def decode(self, message):
        decoded_0 = [0]*len(message)
        decoded_1 = [1]+[0]*(len(message)-1)
        first_ans = ""
        second_ans = ""
        # assume first element is 0
        for i, letter in enumerate(message):
            val = int(letter)
            if len(message)==1:
                if(val>1): #redundant...
                    first_ans = "NONE"
                    second_ans = "NONE"
                if(val!=0):
                    first_ans = "NONE"
                if(val!=1):
                    second_ans = "NONE"

            elif(i==0):
                decoded_0[i+1] = val-0
                decoded_1[i+1] = val-1
            elif(i==len(message)-1):
                if(decoded_0[i]!=val-decoded_0[i-1]):
                    first_ans = "NONE"
                if(decoded_1[i]!=val-decoded_1[i-1]):
                    second_ans = "NONE"
            else:
                decoded_0[i+1] = val-decoded_0[i]-decoded_0[i-1]
                decoded_1[i+1] =val-decoded_1[i]-decoded_1[i-1]

            if(not 0<=decoded_0[i]<=1):
                first_ans = "NONE"
            if(not 0<=decoded_1[i]<=1):
                second_ans = "NONE"
        n = list(map(str, decoded_0))
        m = list(map(str, decoded_1))
        if(first_ans != "NONE"):
            first_ans = first_ans.join(n)
        if(second_ans != "NONE"):
            second_ans = second_ans.join(m)

        return (first_ans, second_ans)

test = BinaryCode()
print(test.decode('123210122'))
print(test.decode('11'))
print(test.decode('1'))
