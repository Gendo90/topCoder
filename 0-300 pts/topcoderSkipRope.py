# Problem Statement
#
# Every schoolgirl (and the occasional schoolboy) likes to skip rope. It's fine to go solo, but it's better still to have partners who can swing the rope and chant along. Ideally, the two children holding the rope are about as tall as the one doing the skipping.
# In this problem, we shall measure height in centimeters. Given a tuple (integer) containing the heights of your prospective partners, return the two that are closest to your own height, which is specified by a separate integer. Break ties in favor of taller candidates, and sort the return values in non-descending order.
# Definition
#
# Class:
# SkipRope
# Method:
# partners
# Parameters:
# tuple (integer), integer
# Returns:
# tuple (integer)
# Method signature:
# def partners(self, candidates, height):

# Gendo90 has submitted the 250-point problem for 162.63 points
#Successful on first try!
class SkipRope(object):
    def partners(self, candidates, height):
        relative_heights = [h-height for h in candidates]
        cand1 = min(abs(a) for a in relative_heights)
        try:
            cand1_Index = relative_heights.index(cand1)
        except:
            cand1_Index = relative_heights.index(-cand1)
        a = relative_heights.pop(cand1_Index)
        cand2 = min(abs(b) for b in relative_heights)
        all_cand2 = [l for l in relative_heights if(l==cand2 or l==-cand2)]
        total_cand2 = len(all_cand2)
        if(total_cand2>1):
            cand2=max(all_cand2)
        try:
            cand2_Index = relative_heights.index(cand2)
        except:
            cand2_Index = relative_heights.index(-cand2)

        b = relative_heights.pop(cand2_Index)
        final = [a+height, b+height]
        final.sort()

        return tuple(final)

test = SkipRope()

print(test.partners((134, 79, 164, 86, 131, 78, 99, 150, 105, 163, 150, 110, 90, 137, 127, 130, 121,
 93, 97, 131, 170, 137, 171, 153, 137, 138, 92, 103, 149, 110, 156), 82))
