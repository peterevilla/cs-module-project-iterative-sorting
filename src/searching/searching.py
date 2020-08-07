def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start_index = 0
    last_index = len(arr) - 1 

    while start_index <= last_index:
        middle_index = start_index + last_index // 2 
        if target == arr[middle_index]:
            return middle_index
        if target > arr[middle_index]:
            start_index = middle_index + 1
        else:
            last_index = middle_index - 1
            




    return -1  # not found
