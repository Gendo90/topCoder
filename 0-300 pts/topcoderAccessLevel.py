# Problem Statement
#
# In many computer systems and networks, different users are granted different levels of access to different resources. In this case, you are given a tuple (integer) rights, indicating the privilege level of each user to use some system resource. You are also given a integer minPermission, which is the minimum permission a user must have to use this resource.
# You are to return a string indicating which users can and cannot access this resource. Each character in the return value corresponds to the element of users with the same index. 'A' indicates the user is allowed access, while 'D' indicates the user is denied access.
# Definition
#
# Class:
# AccessLevel
# Method:
# canAccess
# Parameters:
# tuple (integer), integer
# Returns:
# string
# Method signature:
# def canAccess(self, rights, minPermission):


#Gendo90 has submitted the 250-point problem for 244.60 points
#Successful on first try!
class AccessLevel(object):
    def canAccess(self, rights, minPermission):
        output = ["A" if (user>=minPermission) else "D" for user in rights]

        return "".join(output)

test = AccessLevel()

#workaround that is good to know about!
print(test.canAccess((1,), 20))
# print(test.canAccess(tuple(1), 20))
