import random 
import time 

#iterative complexities 

#Big O notation

# factorial time n! --> worst

# Number of operations 

#Classifications:
# 1- Constant time -- O(1)
# 2 - Logarithimc time -- O(Log N)
# 3 - Linear Time -- O(N)
# 4 - Linearithmic -- O(N * Log N)
# 5 - polynomial time -- O(N^c)
# 6 - Exponential time -- O(c^n)


###### Search ######

    #Linear Search in deck of cards Unordered/Unsorted

my_range = 100
my_size = 10

my_random = random.sample(range(my_range), my_size)
print(my_random)

search_for = 9

# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return True
#         return False

# print(linear_search(my_random, search_for))


    #Binary Search Ordered/Sorted

def find_binary(arr, value):
    first = 0
    last = (len(arr) - 1)

    found = False

    while first <= last and not found:
        middle = first + last // 2

        if arr[middle] == value:
            found = True
        else:
            if value < arr[middle]:
                last = middle - 1
            else:
                first = middle + 1
    return found

print(find_binary(my_random, search_for))





#Insertion Sort

def insertion_sort(list_of_sort):

    for i in range(len(list_of_sort)):
        temp = list_of_sort[i]
        j = i

        while j > 0 and temp < list_of_sort[j - 1]:
            list_of_sort[j] = list_of_sort[j-1]
            j -= 1
        list_of_sort[j] = temp

    return list_of_sort

print(insertion_sort(my_random))