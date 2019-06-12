# Problem Statement
#     Let's walk around the clock. We start at twelve o'clock and flip a coin. If it comes up heads, we step forward by one hour. If it's tails, we step one hour backward. We flip the coin a second time, but now we step two hours forward in the case of heads, or two hours backward for tails. On the third flip, we step three hours forward or backward on the same principle. In general, then, the nth flip decides the direction in which we step n hours: we move forward on heads, and backward on tails.
# You are given a string describing a sequence of coin flips such that the nth character is either 'h', meaning that the nth flip is heads, or 't' to signify that the nth flip is tails. Return the hour at which we end up by following the above procedure.
# Definition
#
# Class:
# ClockWalk
# Method:
# finalPosition
# Parameters:
# string
# Returns:
# integer
# Method signature:
# def finalPosition(self, flips):
#
# Limits
#
# Time limit (s):
# 2.000
# Memory limit (MB):
# 64

# Gendo90 has submitted the 250-point problem for 223.31 points
#Successful on first try!
class ClockWalk(object):
    def finalPosition(self, flips):
        clock_nums = [hour for hour in range(1, 12)]
        clock_nums.insert(0, 12)
        steps = 1
        position = [0]
        flips = [n for n in flips]
        while(flips):
            this_move = flips.pop(0)
            if(this_move == 'h'):
                newHour = (steps+position[steps-1])%12
            else:
                newHour = (position[steps-1]-steps)%12

            position.append(newHour)
            steps+=1

        return clock_nums[position[-1]]

test = ClockWalk()

print(test.finalPosition("hhthh"))
