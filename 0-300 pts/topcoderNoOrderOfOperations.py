# Problem Statement
#
# When evaluating a mathematical expression, there is the possibility of ambiguity. If you wanted to know the result of "3 + 5 * 7", you might first evaluate the (3+5) and get 56, or first evaluate the (5*7) and get 38. This ambiguity can be resolved by using the order of operations: first do multiplication and division (from left to right), and then after all those are done, do addition and subtraction (again from left to right). Here, the correct result would be the 38.
# While this is unambiguous, it certainly is somewhat annoying. You think it would be easier if people did all math from left to right, all the time, and want to make a simple expression evaluator to do so.
# The expression will be given to you as a string expr. It will consist of one digit numbers (0 through 9) alternating with operators (+, -, or *), with no spaces between them. Thus, expr would follow the format Digit Operator Digit Operator .... Digit. For example, the expression given above would be given as "3+5*7".
# Your method should return an int representing the value of the expression when evaluated from left to right.
# Definition
#
# Class:
# NoOrderOfOperations
# Method:
# evaluate
# Parameters:
# string
# Returns:
# integer
# Method signature:
# def evaluate(self, expr):

##Server was not working for grading - invalid points
#(does accept my answer now, though)
#Successful on first try!
class NoOrderOfOperations(object):
    def evaluate(self, expr):
        val = int(expr[0])
        operator = ""

        if(len(expr)!=1):
            for item in expr[1:]:
                try:
                    isinstance(int(item), int)
                    if(operator=="+"):
                        val+=int(item)
                    elif(operator=="-"):
                        val-=int(item)
                    elif(operator=="*"):
                        val*=int(item)
                    elif(operator=="/"):
                        val/=int(item)
                except:
                    operator = item

        return val





test = NoOrderOfOperations()

print(test.evaluate("1*2*3*4*5*6*7*8*9"))
