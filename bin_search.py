

def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

# Example setup

# my_list = [1, 2, 3, 4, 5, 6, 8, 9, 10]
#
# print (binary_search(my_list, 3)) # => 2
#
# print (binary_search(my_list, -1)) # None
