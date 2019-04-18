class A0Paper():
    def canBuild(self, A):
        arr = list(A)
        if arr[0]>=1:
            return 'Possible'
        n = len(arr)
        #print(arr)
        for i in range(n-1, 0, -1):
            z = arr[i]//2
            arr[i-1] += z
            arr[i] = arr[i]-z*2

        if arr[0]>=1:
            return 'Possible'
        else:
            return 'Impossible'

l = A0Paper()

print(l.canBuild((0, 3)))
print(l.canBuild([1, 0]))
print(l.canBuild([0, 0, 1, 5]))
