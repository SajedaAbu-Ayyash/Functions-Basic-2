# 1.Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
def Countdown():
    list = []
    for i in range(5, -1, -1):
        list.append(i)
        return list
    num = Countdown()
    print(num)

# 2.Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
def print_and_return():
    print(list[0])
    return list[1]
result = print_and_return([0, 1])
print(result)

# 3.First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def first_plus_length():
    return list[0] + len(list)
result = first_plus_length([1,2,3,4,5])
print("result: " + result)

# 4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
def values_greater_than_second (list):
    if len(list) < 2:
        return False
    second_value = list[1]
    new_list = []
    for i in list:
     if i > second_value:
      new_list.append(i)
    print(len(new_list))
    return new_list
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))


