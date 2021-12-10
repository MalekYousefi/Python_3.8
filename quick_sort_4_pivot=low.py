def partition(A, low, high):
    i=low
    j=high
    pivot=A[low]
    while(i<j):
        while(A[i]<=pivot):
            i+=1
            if(i==high):
                break
        while(A[j]>=pivot):
            j-=1
            if(j==low):
                break
        if(i<j):
            A[i], A[j]=A[j], A[i]
    A[low], A[j]=A[j], A[low]
    return j
#=========================================
def quicksort(A, low, high):
    if(low<high):
        j=partition(A, low, high)
        quicksort(A, low, j-1)
        quicksort(A, j+1, high)
#=========================================
lst=[int(i) for i in input().split(" ")]
low=0
high=len(lst)
quicksort(lst, low, high-1)
for i in range(0, len(lst)):
    print(lst[i], "", end="")