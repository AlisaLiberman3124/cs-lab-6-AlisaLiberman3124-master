def checkMinHeap(A, i):
    if 2 * i + 2 > len(A):
        return True
    left = (A[i] <= A[2 * i + 1]) and checkMinHeap(A, 2 * i + 1)
    right = (2 * i + 2 == len(A)) or (A[i] <= A[2 * i + 2] and checkMinHeap(A, 2 * i + 2))
    return left and right

f = open("input.txt", "r")
d = open("output.txt", "w")
n = int(f.readline())
a = list(f.readline().split())
i = 0
if checkMinHeap(a, i):
    d.write(str("YES"))
else:
    d.write(str("NO"))
