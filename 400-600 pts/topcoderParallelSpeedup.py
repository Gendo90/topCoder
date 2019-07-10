# Problem Statement
#
# Your boss thinks you can speed up an application you are writing by running it on multiple processors in parallel. Your application performs k independent tasks that each take 1 millisecond to run on a single processor. Distributing a task across several processors does not make it run faster, but running different tasks on different processors may indeed make your application faster.
# Unfortunately, when your application runs on more than one processor, communication overheads between processors become a significant factor. In particular, every pair of processors spends overhead milliseconds communicating with each other before work on the tasks can begin. Worse, because the processors share a single bus for communications, different pairs of processors cannot communicate in parallel. For example, if overhead is 2 milliseconds and you run your application on 3 processors, there will be a 6 millisecond delay before the actual computations begin: 2 milliseconds for processors 1 and 2 to communicate, 2 milliseconds for processors 1 and 3 to communicate, and 2 milliseconds for processors 2 and 3 to communicate. Note that, once the initial communications phase has completed, no further communications are required, even if each processor is executing multiple tasks.
# Your task is to determine the number of processors that will run the k tasks in the minimum amount of time, assuming overhead milliseconds of communication overhead per pair of processors. If several configurations of processors will achieve the minimum amount of time, prefer the configuration with the smallest number of processors.
# Definition
#
# Class:
# ParallelSpeedup
# Method:
# numProcessors
# Parameters:
# integer, integer
# Returns:
# integer
# Method signature:
# def numProcessors(self, k, overhead):

# Gendo90 has submitted the 500-point problem for 324.99 points (first submission)
# kept having one problem wrong until the last submission (150 pts)
# Successful on fourth try - but some of those were adding the 1.0 multipliers
# and the problems worked on my computer. I did need to do some rounding,
# though, according to how the problem works. Need to look for that more in
# the future, if there are "equivalent" cases after rounding
class ParallelSpeedup(object):
    def numProcessors(self, k, overhead):
        #dynamic programming!
        time_taken = []

        time_taken.append(k)
        val = k*1.0/2 + overhead
        if(val!=int(val)):
            val = int(val)+1
        time_taken.append(val)

        n = 3
        while(time_taken[-1]<time_taken[-2]):
            this_time = k*1.0/n+((n*1.0*(n-1))/(2.0))*(overhead)
            if(this_time != int(this_time)):
                this_time = int(this_time)+1
            time_taken.append(this_time)
            n+=1
            # print(time_taken)

        fastest = min(time_taken)
        num_processors = time_taken.index(fastest)+1
        print(time_taken)

        return num_processors


test = ParallelSpeedup()

print(test.numProcessors(21, 10))
