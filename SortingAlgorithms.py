import math
# Sorting algorithms

# Insertion SORT
def insertion_sort(A, n):
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while (j >= 0) & (A[j] > key):
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = key
    return A

B = [31, 41, 59, 26, 41, 58]
n = len(B)

print('Insertion sort: ', insertion_sort(B, n))

# Merge Sort
def merge(A, p, split, r):
    n_l = split - p + 1
    n_r = r - split

    L = []
    R = []

    for i in range(0, n_l):
        L.append(A[p + i])
    for j in range(0, n_r):
        R.append(A[split + j + 1])
    
    i = 0
    j = 0
    k = p

    while (i < n_l) & (j < n_r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

        k = k + 1

    while i < n_l:
        A[k] = L[i]
        i = i + 1
        k = k + 1

    while j < n_r:
        A[k] = R[j]
        j = j + 1
        k = k + 1

def merge_sort(A, p, r):
    if p < r:
        split = math.floor((p+r)/2)

        merge_sort(A, p, split)
        merge_sort(A, split+1, r)

        merge(A, p, split, r)

    return A

# Result
print('Merge sort: ', merge_sort(B, 0, n-1))


# Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))