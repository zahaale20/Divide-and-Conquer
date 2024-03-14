# Alex Zaharia (azaharia@calpoly.edu)
# CSC 349
# Lab 1: Singleton

import sys

# Main
def main():
    filename = sys.argv[1] # take singleton list from second element (index 1) of terminal input
    #filename1 = "unique-64" # take singleton list from project folder
    #filename2 = "unique-180" # take singleton list from project folder
    file = open(filename, "r") # open file
    nums = [] # create list to store numbers (pairs and unique singleton)
    for line in file: # iterate through lines (the numbers) in file
        nums.append(int(line)) # append line (a number) to the list
    file.close() # close the file
    singleton = findSingleton(nums, 0, len(nums) - 1) # calculate singleton
    print(singleton) # print singleton

# Singleton
def findSingleton(nums, left, right):
    if left == right:  # if at left and right indices are at the same index...
        return nums[left] # return element at either left or right indices

    # set middle element into a var 'mid'
    mid = (left + right) // 2 # get midpoint

    # Base Case
    if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]: # if the middle element is not equal to its neighbors...
        return nums[mid] # return the middle element, we know it is unique

    # ELSE...

    # Recursive Case (Breakdown the problem into subproblems)
    if mid % 2 == 0: # we check if middle index is even or odd to know where the element is in relation to its pair (if it has one)
        if nums[mid] == nums[mid - 1]:  # we check if the middle element is equal to the previous element
            return findSingleton(nums, left, mid - 2) # if so, we recursively call the left half of the list
        return findSingleton(nums, mid + 2, right)  # else, check left side of the list

    # else if the middle index is odd
    if nums[mid] == nums[mid - 1]: # if middle element == previous element
        return findSingleton(nums, mid + 1, right) # call singleton on the right half of the list
    return findSingleton(nums, left, mid - 1) # call singleton on the left half of the list


if __name__ == "__main__":
    main()
