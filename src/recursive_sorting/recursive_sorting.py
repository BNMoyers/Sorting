# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    merged_arr = []
    # TO-DO
    # starting at beginning of `arrA` and `arrB`
    listA = 0
    listB = 0
    
    # compare the next value of each
    while listA < len(arrA) and listB < len(arrB):
        if arrA[listA] <= arrB[listB]:
    # add smallest to `merged_arr`
            merged_arr.append(arrA[listA])
            listA +=1
        else:
            merged_arr.append(arrB[listB])
            listB +=1    
    # if arrB is empty:
    while listA < len(arrA):
        merged_arr.append(arrA[listA])
        listA +=1
    #if arr A is empty:
    while listB < len(arrB):
        merged_arr.append(arrB[listB])
        listB +=1     

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
import math
def merge_sort( arr ):
    # TO-DO
    if len(arr) >1:
        #find the midpoint and divide LHS from RHS
        midpoint = int(math.floor(len(arr)/2))
        LHS = arr[0:midpoint]
        RHS = arr[midpoint:len(arr)]
        # recursively call merge_sort() on LHS
        arrA = merge_sort(LHS)
        # recursively call merge_sort() on RHS
        arrB = merge_sort(RHS)
        # merge sorted pieces
        return merge(arrA, arrB)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
