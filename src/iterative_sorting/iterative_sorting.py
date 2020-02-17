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
    #keep track of whether a swap occured in the last pass
    did_swap = True
    #while loop comparing each item to the adjacent item.
    while did_swap == True:
        #set did_swap to false
        did_swap = False
        #iterate over list
        for i in range(0,len(arr)-1):
            #check if elements should be swapped
            if arr[i] > arr[i+1]:
                #if so, swap them and note that swap=true
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                did_swap = True
               
            
                     
    return arr


# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr