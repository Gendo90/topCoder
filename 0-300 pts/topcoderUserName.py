# Problem Statement
#
# You are implementing the member registration system of an online dating site. When a new member signs up, it is possible that she initially chooses the same username as an existing member. The system must then inform the new member of the conflict and suggest a variant of the chosen name with a number attached to the end.
# If an existing member is named "FunkyMonkey", for example, and a new member wants the same username, the simplest suggestion the system can make is "FunkyMonkey1". If there is already a member by that name, the system must suggest "FunkyMonkey2", unless that variant is also taken. If all names from "FunkyMonkey1" through "FunkyMonkey9" are taken as well as the original "FunkyMonkey", the system moves on to consider "FunkyMonkey10", and so on. The goal is to use the smallest possible number in the variant. Note that each username consists of letters (the characters from 'a' to 'z' and from 'A' to 'Z') and numerals ('0' to '9').
# You are given a tuple (string), existingNames, containing all usernames that have already been registered in the system. You are also given a single string, newName, containing the username that a new member wants to use. In the event of a conflict, this member will accept the suggestion offered by your system in accordance with the principles above. Return a string containing the username finally assigned to the new member.
# Definition
#
# Class:
# UserName
# Method:
# newMember
# Parameters:
# tuple (string), string
# Returns:
# string
# Method signature:
# def newMember(self, existingNames, newName):

#Gendo90 has submitted the 250-point problem for 232.35 points
#Successful on first try!
class UserName(object):
    def newMember(self, existingNames, newName):
        if(newName in existingNames):
            newName=newName+str(1)
        curr_num=1
        while(newName in existingNames):
            curr_num+=1
            newName = newName.replace(str(curr_num-1), str(curr_num))

        return newName


test = UserName()

print(test.sum("-----Abc"))
