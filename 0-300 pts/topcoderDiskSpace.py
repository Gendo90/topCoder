#Problem Statement
#    
#As of late, your usually high-performance computer has been acting rather sluggish. You come to realize that while you have plenty of free disk space on your machine, it is split up over many hard drives. You decide that the secret to improving performance is to consolidate all the data on your computer onto as few hard drives as possible.
#Given a tuple (integer) used, representing the amount of disk space used on each drive, and a corresponding tuple (integer) total, representing the total capacity of each drive mentioned in used, you should attempt to pack the data onto as few hard drives as possible. You may assume that the data consists of very small files, such that splitting it up and moving parts of it onto different hard drives never presents a problem. Return the minimum number of hard drives that still contain data #after the consolidation is complete.
#Definition
#    
#Class:
#DiskSpace
#Method:
#minDrives
#Parameters:
#tuple (integer), tuple (integer)
#Returns:
#integer
#Method signature:
#def minDrives(self, used, total):

#Gendo90 has submitted the 250-point problem for 75.00 points
#Took a few tries, must have missed a trick or something...
#Maybe look at it again later? Looks like the knapsack problem, use dynamic
#programming or greedy algorithms

class DiskSpace(object):
    def minDrives(self, used, total):
        num_hds = len(total)
        used = list(used)
        total = list(total)
        together = zip(used, total)
        space_available = sum(x[1]-x[0] for x in together)
        mod_space = min(used)
        last_full = False
        #print(mod_space)

        while(space_available>=mod_space and not last_full):
            pusher = max(total)
            max_ind = total.index(pusher)
            takeoff = min(total)
            min_ind = total.index(takeoff)
            min_used = used[min_ind]
            total.pop(min_ind)
            used.pop(min_ind)
            for i in range(len(total)):
                space = total[i]-used[i]
                if(min_used>=space):
                    used[i] = total[i]
                else:
                    used[i] = total[i]-(space-min_used)
                min_used = max(min_used - space, 0)
                if(min_used==0):
                    #total.insert(min_ind, takeoff)
                    #used.insert(min_ind, 0)
                    break
            if(min_used!=0):
                total.insert(min_ind, takeoff)
                used.insert(min_ind, min_used)
            together = zip(used, total)
            #print(used, total)
            space_available = sum(x[1]-x[0] for x in together)
            #print(space_available)
            mod_space = min(used)
            min_loc = used.index(mod_space)
            #print(total[min_loc]-mod_space)
            used.pop(min_loc)
            if(len(total) == 1 or space_available == total[min_loc]-mod_space and not any(x for x in used if x<=space_available)):
                last_full = True
            used.insert(min_loc, mod_space)

        together = zip(used, total)
        #print(list(together))
        n = len(list(together))

        return n


test = DiskSpace()

print(test.minDrives((150, 1, 1), (150, 150, 500)))
