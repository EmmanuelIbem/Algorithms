# I will be implementing a binary search in python with comments to explain each step. I will also throw in frequent uses.

# This is the iterative implementation of binary search

def find_index(elements,value):
    left = 0       #set the lowerbound to index 0
    right = len(elements) -1   #set the upperbound to the highest index

    while left <= right:
        middle = (left + right) // 2    # we define the middle as the average between the left and right

        # This is how we find the value we are looking for as well as updating the upper and lower bound

        if elements[middle] == value:
            return middle
        
        if elements[middle] < value:
            left = middle + 1   # if the value is greater than the middle, we move up our lower bound
        elif elements[middle] > value:
            right = middle -1   # If the value is smaller than the upper bound, reduce the upper bound from the middle
    
 



