# 1. Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element)
def count_down(number):
    new_list = []
    for x in range(number, -1, -1):
        new_list.append(x)
    return new_list

# print(count_down(5))
# print(count_down(15))

# 2. Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
def print_and_return(list):
    print(list[0])
    return list[-1]

# print(print_and_return([6,8]))
# print(print_and_return([5,9]))

# 3 First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def sum_with_length(list):
    sum = 0;
    sum = list[0] + len(list)
    return sum

# print(sum_with_length([3,5,7,3]))
# print(sum_with_length([1,5,8]))

# 4 Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
def values_greater_than_second(list):
    new_list = []
    if (len(list) >= 2):
        for x in list:
            if (x > list[1]):
                new_list.append(x)
        print(len(new_list))
        return new_list
    else:
        return False
    
# print(values_greater_than_second([5,2,3,2,1,4]))
# print(values_greater_than_second([3]))

# 5 This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

def size_list(size, value):
    new_list = []
    for x in range(0, size):
        new_list.append(value)
    return new_list

# print(size_list(4,7))
# print(size_list(6,2))