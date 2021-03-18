# The Solution here assumes that all elements in the input list are distinct

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array
    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return recursive_search_func(input_list, number, 0 , len(input_list)-1)

def recursive_search_func(input_list, number, start_position, end_position):
    middle = (start_position + end_position) // 2
    #print(start_position, end_position)
    if start_position > end_position:
        return -1
        
    if input_list[middle] == number:
        return middle

    if input_list[middle] <= input_list[end_position]:
        if number >= input_list[middle] and number <= input_list[end_position]:
            return recursive_search_func(input_list, number, middle+1, end_position)
        else:
            return recursive_search_func(input_list, number, start_position, middle-1)
    elif number >= input_list[middle] or number <= input_list[end_position]:
        return recursive_search_func(input_list, number, middle+1, end_position)
    else:
        return recursive_search_func(input_list, number, start_position, middle-1)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6))
#expected output: 0
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
print('----------------------------------------')

print(rotated_array_search([4, 7, -10, -6, -5, -4, 0, 2],-10))
#expected output: 2
test_function([[4, 7, -10, -6, -5, -4, 0, 2],-10])
print('----------------------------------------')

print(rotated_array_search([-25, -20, -9, -1, 0, 1, 3, 10, 18, 34, 45, 70, -100, -76, -34],-100))
#expected output : 12
test_function([[-25, -20, -9, -1, 0, 1, 3, 10, 18, 34, 45, 70, -100, -76, -34],-100])
print('----------------------------------------')

print(rotated_array_search([-25, -20, -9, 0, 1, 3, 10, 18, -100],25))
#expected output : -1
test_function([[-25, -20, -9, 0, 1, 3, 10, 18, -100],25])
print('----------------------------------------')

print(rotated_array_search([],17))
#expected output : -1
test_function([[],17])
print('----------------------------------------')