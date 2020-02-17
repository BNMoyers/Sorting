# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        #set current index
        cur_index = i
        #default the smallest index to the current index (starts as first item in array)
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        #set another loop which runs from current index to the end
        # whenever a number is smaller than the value in the smallest index(defaults to current index) , update the smallest index variable
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j   



        # TO-DO: swap
        #assign the smallest index to a temporary variable
        temp = arr[smallest_index]
        #set the smallest index to equal the current index
        arr[smallest_index] = arr[cur_index]
        #update the current index to equal the value held in the temp variable
        arr[cur_index] = temp



    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr