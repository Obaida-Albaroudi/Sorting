# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[smallest_index]):
                smallest_index=j
        arr[cur_index],arr[smallest_index]= arr[smallest_index],arr[cur_index]
        # TO-DO: swap

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if (arr[j]>arr[j+1]):
                arr[j], arr[j+1]= arr[j+1],arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

x=[1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
bubble_sort(x)