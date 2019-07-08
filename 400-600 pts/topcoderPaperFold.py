# Problem Statement
#
# You have a piece of paper that you need to fold to fit into a box with a given width and length. Each time you fold the paper, you can fold it in half across either its width or length, but you can only fold the paper 8 times (after 8 times, the paper is too dense to fold again).
# You will be given a tuple (integer) paper, which contains the width and length of the paper in inches, and a tuple (integer) box, which contains the width and length of the box in inches. In both cases, the first element is the width and the second element is the length. Your method should return the fewest number of folds which would allow you to fit the paper into the box. You can rotate the paper 90 degrees if it will fit with fewer folds, but the paper must lie completely flat inside the box. If the paper cannot be fit into the box with 8 folds or fewer, return -1.
# Definition
#
# Class:
# PaperFold
# Method:
# numFolds
# Parameters:
# tuple (integer), tuple (integer)
# Returns:
# integer
# Method signature:
# def numFolds(self, paper, box):

# Gendo90 has submitted the 500-point problem for 351.86 points
# Successful on 1st try!
# Could have done one loop to check both conditions, maybe, but would not
# have been able to break, just stop counting - could have also made a function
# and just flipped inputs...
class PaperFold(object):
    def numFolds(self, paper, box):
        #normal orientation
        folds_reg = 0
        reg_fold = list(paper)
        i=0
        norm_works = False
        while(i<8):
            if(box[0]<reg_fold[0]):
                reg_fold[0]/=2.0
                folds_reg+=1
            elif(box[1]<reg_fold[1]):
                reg_fold[1]/=2.0
                folds_reg+=1
            # print(reg_fold)
            # print(folds_reg)

            if(box[0]>=reg_fold[0] and box[1]>=reg_fold[1]):
                norm_works = True
                break

            i+=1

        #rotated orientation
        folds_rot = 0
        rot_fold = list(paper)
        i=0
        rot_works = False
        while(i<8):
            if(box[1]<rot_fold[0]):
                rot_fold[0]/=2.0
                folds_rot+=1
            elif(box[0]<rot_fold[1]):
                rot_fold[1]/=2.0
                folds_rot+=1

            if(box[1]>=rot_fold[0] and box[0]>=rot_fold[1]):
                rot_works = True
                break

            i+=1

        if(norm_works and rot_works):
            return min(folds_reg, folds_rot)
        elif(norm_works):
            return folds_reg
        elif(rot_works):
            return folds_rot
        else:
            return -1





test = PaperFold()

print(test.numFolds((11, 17), (6, 4)))
