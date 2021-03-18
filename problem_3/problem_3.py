def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.
    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    frequency = [0 for i in range(10)]
    for i in input_list:
        frequency[i]+= 1

    first_number, second_number = 0,0
    first = True
    for i in range(10):
        while frequency[9-i] > 0:
            if first:
                first_number *= 10
                first_number += 9-i
                first = False
            else:
                second_number *= 10
                second_number += 9-i
                first = True
            frequency[9-i] -= 1
    return (first_number, second_number)
    
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_case_0 = [[1, 2, 3, 4, 5], [542, 31]]
test_case_1 = [[4, 6, 2, 5, 9, 8], [964, 852]]

test_case_2 = [[8], [8, 0]]
test_case_3 = [[], [0, 0]]


print(rearrange_digits(test_case_0[0]))
#expected output: (531, 42)
test_function(test_case_0)
print('---------------------------------------')


print(rearrange_digits(test_case_1[0]))
#expected output: (964, 852)
test_function(test_case_1)
print('---------------------------------------')


print(rearrange_digits(test_case_2[0]))
#expected output: (8,0)
test_function(test_case_2)
print('---------------------------------------')


print(rearrange_digits(test_case_3[0]))
#expected output: (0,0)
test_function(test_case_3)
print('---------------------------------------')