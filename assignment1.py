# Name: Ted Janney
# OSU Email: janneyt@oregonstate.edu
# Course:      CS261 - Data Structures
# Assignment: 1
# Due Date: 19/4/2022
# Description: Methods for StaticArray, including min and max finding, reversing, and sorting with helper functions


import random
from static_array import *
import big_o


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> tuple:
    '''
    Takes a static array and returns the maximum and minimum values in O(n) time.
    :param arr: StaticArray instance
    :return: a tuple, the minimum value followed by the maximum value
    '''
    minimum = None
    maximum = None


    # For time complexity of O(n), we need to only use one for loop
    for indices in range(0,arr.length()):
        current_item = arr[indices]

        # Set minimum and maximum on first iteration
        if indices == 0:
            minimum = current_item
            maximum = current_item

        # For all other indices, maximum and minimum will diverse
        elif current_item < minimum:
            minimum = current_item

        elif current_item > maximum:
            maximum = current_item

    return tuple((minimum, maximum))
# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    '''
    Takes a static array of integers and reworks according to the classic fizzbuzz procedure.
    :param arr: StaticArray of integers
    :return: new StaticArray of integers AND strings
    '''

    arr_length = arr.length()

    new_arr = StaticArray(arr_length)

    for indices in range(0,arr_length):
        if arr[indices] % 3 == 0 and arr[indices] % 5 == 0:
            new_arr[indices] = "fizzbuzz"
        elif arr[indices] % 5 == 0:
            new_arr[indices] = "buzz"
        elif arr[indices] % 3 == 0:
            new_arr[indices] = "fizz"
        else:
            new_arr[indices] = arr[indices]
    return new_arr

# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    '''
    Takes a StaticArray and reverses the elements in place.
    :param arr: a StaticArray
    :return: the same static array with the elements in the reverse order
    '''

    arr_length = arr.length()

    # A head and tail index are both required for my algorithm to work
    arr_head = 0
    arr_tail = arr.length()-1

    # Temporary variable for later on
    blank = None
    for indices in range(0,arr_length//2):

        # Save the current head, swap the tail's value into the head position, swap the blank value into the tail position
        blank = arr[arr_head]
        arr[arr_head] = arr[arr_tail]
        arr[arr_tail] = blank
        arr_head += 1
        arr_tail -= 1

    return arr
# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    '''
    Rotates elements in a StaticArray a specific number of spots left or right
    :param arr: the StaticArray that needs to be rotated
    :param steps: The number of steps and the directionality of the rotation
    :return: a new StaticArray with the rotated indices value
    '''

    negative = False
    arr_length = arr.length()
    new_arr = StaticArray(arr_length)
    if steps < 0:
        negative = True
    for indices in range(0,arr_length):

        if not negative and steps >= arr_length:

            # Because we can call the function with a number of steps exceeding the length of the array
            # We must regularize it using modulo
            new_steps = steps % arr_length
            new_index = indices + new_steps
        elif not negative and steps <= arr_length:
            new_index = indices + steps
        elif negative and (-1*steps) >= arr_length:

            # Same regularization as with positive indices
            new_steps = steps % arr_length
            new_index = indices + new_steps
        elif negative:
            new_index = indices + steps

        # Positive step condition to avoid index out of range error
        if new_index >= arr_length:
            new_index = new_index - arr_length
        # Negative step condition could cause index out of range error
        elif new_index < 0:
            new_index = arr_length + new_index
        new_arr[new_index] = arr[indices]
    return new_arr


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """

    Takes a start value and an end value and generates all consecutive integers between the two values. Stored in
    a new StaticArray.

    :param start: integer, the included first value
    :param end: integer, the included final value
    :return: a StaticArray containing all consecutive integers in the StaticArray, of size (start-end) +1 or equivalent
        depending on direction of iterating.
    """

    # I have separate processing for sequences beginning with a start value and decrementing to reach the end
    # Versus those starting with a start value and *incrementing*. This is controlled by the direction variable
    if start < end:
        new_arr = StaticArray(end-start + 1)
        direction = 1
    elif end < start:
        new_arr = StaticArray(start-end + 1)
        direction = -1
    elif end == start:
        # I'm choosing to simply return this edge case
        new_arr = StaticArray(1)
        new_arr[0] = start
        return new_arr
    count = 0

    # Since the end value has to be inclusive, the range is from start to end+1. Similarly, the direction variable
    # controls positive vs negative for loop iterating
    for consec_ints in range(start, end+1,direction):
        new_arr[count] = consec_ints
        count += 1

    return new_arr

# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    '''
    Tests whether a StaticArray is sorted or not.

    In order to meet the time complexity, I first process 3 special cases, arrays of length 1-3. This allows me
    to do a "normal processing" of arrays by using a windows of the current index and the two spots adjacent
    to check for descending or ascending tendencies. If there's a "dip", where index i > i-1 AND i > i+1 or
    the opposite, where index i < i-1 AND i < i+1, then we can immediately discard. Once all dips are guaranteed
    not in the array, we just return the basis of comparing a single index pair.

    :param arr: a StaticArray
    :return: integer. Possible values: 1 for ascending order, -1 for descending order, 0 for unsorted
    '''
    arr_length = arr.length()

    # I've identified 2 special cases, arrays of length 1 and 2.

    if arr_length == 1:
        return 1

    elif arr_length == 2 and arr[0] < arr[1]:
        return 1

    elif arr_length == 2 and arr[0] > arr[1]:
        return -1


    # For lengths 4 or more
    for indices in range(1, arr_length-1):

        # These are the "dips" that indicate unsorted
        if arr[indices] <= arr[indices +1] and arr[indices] <= arr[indices-1]:
            return 0
        elif arr[indices] >= arr[indices+1] and arr[indices] >= arr[indices-1]:
            return 0

    # Having guaranteed there's no dips, we can perform a single comparison and return
    if arr[0] <= arr[1]:
        return 1
    elif arr[1] <= arr[0]:
        return -1
    return 0

# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> tuple:
    """

    """
    count = 1
    current_freq = 0
    mode = -1
    for indices in range(1, arr.length()):

        # Indicates we've discovered a unique value
        if arr[indices] != arr[indices - 1]:
            current_freq = count
            count = 1
            mode = arr[indices]

        # Simply increases the current value's frequency count
        elif arr[indices] == arr[indices - 1]:
            count += 1

    # If the very final value exceeds the frequency count, it won't be caught in the for loop due to
    # how the range function is not inclusive of the end value. So, special case processing.
    if count > current_freq:
        current_freq = count
        mode = arr[indices]
    return tuple((mode, current_freq))
# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    '''
    Removes any duplicate values from a StaticArray
    :param arr: a StaticArray
    :return: a new StaticArray, with duplicates removed
    '''
    new_arr = StaticArray(arr.length())

    # Since the for loop is set to begin iterating on 1, we set the initial index as that index cannot, by
    # definition, already be a duplicate.
    new_arr[0] = arr[0]
    count = 1

    for indices in range(1, arr.length()):

        # Why start iterating at index 1? So this "window" works without index out of bound errors
        if arr[indices] != arr[indices-1]:
            new_arr[count] = arr[indices]
            count += 1
    return new_arr

# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """
    Takes an unsorted StaticArray, generates a count of all integers in the array, and then sorts the original array

    :param arr: an unsorted StaticArray
    :return: the same StaticArray, but sorted
    """
    new_arr = StaticArray(arr.length())
    start, end = min_max(arr)
    possible_integers = sa_range(start, end)
    pos_int_length = possible_integers.length()
    counts = StaticArray(pos_int_length)

    """
    The n+k complexity is as follows. First you iterate over n input, calculate an index, and assign a count
    in a new array.
    
    THEN you iterate over the counts array (size k or smaller) and reassign the values from the original array 
    to a new array based on the counts in the count array. 
    """
    for integers in range(0, arr.length()):
        index = reflect_indices(arr[integers], pos_int_length, end)

        # This actually creates the counts array, which will include blank spaces in most cases
        if counts[index] is None:
            counts[index] = 1
        else:
            counts[index] += 1

    place = 0
    # This unpacks the counts array and assigns values to the new array based on values in the possible_integers array
    for integer in range(0, counts.length()):
        if counts[integer] is not None:
            for count in range(0,counts[integer]):
                new_arr[place+count] = possible_integers[integer]
            place += counts[integer]

    return new_arr

def reflect_indices(cur_num:int, length:int, end:int) -> int:
    """
    Calculates the index of cur_num based on where in the sorted, consecutige integer array cur_num falls
    :param cur_num: the number. Must be in range end-len <= cur_num <= end
    :param length: length of the sorted consecutive integer array
    :param end: final value in the sorted, consecutive integer array
    :return: index of cur_num, integer
    """
    if cur_num <= end and cur_num >= end-length:

        # Intermediate value, this tells us the distance between end and cur_num
        intermediate = end-cur_num
        # Length is actually the final index + 1 (length does not use zero indexing)
        length = length -1

        # The new length value is the index of the value end, so the index of cur_num is length - intermediate
        return length - intermediate
    return False

# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    Takes a sorted StaticArray, squares the contents, and then loads the contents into a new Static Array.
    :param: arr, a StaticArray

    General approach: Iterate once over the array, divide integers into a positive and a negative sublist.
    Iterate again over the integers from original array (via the sublists) and this time put into the returned
    array. Iterate backwards over negative sublist due to how digits are stored in a "sorted" array.

    Time complexity would be 2n (iterate twice, but only twice, over array). Thus, O(n).
    """
    new_arr = StaticArray(arr.length())
    neg_arr = StaticArray(arr.length())
    neg_count = 0
    pos_arr = StaticArray(arr.length())
    pos_count = 0
    negative = False

    # Create negative and positive sublists
    for indices in range(0,arr.length()):

        # There's an odd behavior with Python's ** operator where -1**-1 returns -1. So I'm manually squaring.
        value = arr[indices] * arr[indices]

        # Divide into positive and negative sublists
        if arr[indices] < 0:
            neg_arr[neg_count] = value
            neg_count +=1

            # Boolean used to simplify processing of an array containing only values >= 0.
            negative = True
        else:
            pos_arr[pos_count] = value
            pos_count += 1

    # In the case where negative numbers exist, we have to be wary of two things. The first is that negative
    # numbers, when squared, will have their largest value first, not last. The second is that the positive and
    # and negative arrays almost always contain None values
    if negative:
        pos_index = 0

        # Start negative number processing at the *last* value
        neg_index = neg_count -1
        new_index = 0

        # Process positive array forwards and maintain the new array's index as well
        while (pos_index < arr.length () and new_index < arr.length ()):

            if pos_arr[pos_index] is None:

                # The first None value indicates all remaining values are None. Set the pos_index to the exit
                # condition and only work on the negative array from here on out
                pos_index = arr.length () - 1
                new_arr[new_index] = neg_arr[neg_index]
                neg_index -= 1

            # Compare the positive and negative arrays, put the lower value into the new array first
            # The negative index isn't included in the while conditions, so we also have to check that it is valid
            # (zero or greater)
            elif neg_index < 0 or pos_arr[pos_index] <= neg_arr[neg_index]:
                new_arr[new_index] = pos_arr[pos_index]
                pos_index += 1
            elif neg_arr[neg_index] < pos_arr[pos_index]:
                new_arr[new_index] = neg_arr[neg_index]
                neg_index -= 1

            # No matter what, increment new_index
            new_index += 1
        return new_arr
    elif not negative:
        # Since we only set the negative flag if a negative value was detected, we can guarantee that pos_arr
        # *is* the desired new arr.
        return pos_arr


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":


    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')

