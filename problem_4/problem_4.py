def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
    Args:
       input_list(list): List to be sorted
    """
    idx = 0
    m_idx = 0
    n_idx = len(input_list)-1
    
    while idx <= n_idx:
        if input_list[n_idx] == 2:
            n_idx -= 1
            continue
        if input_list[idx] == 0:
            input_list[idx] = input_list[m_idx]
            input_list[m_idx] = 0
            idx += 1
            m_idx += 1
        elif input_list[idx] == 2:
            input_list[idx] = input_list[n_idx]
            input_list[n_idx] = 2
            n_idx -= 1
        else:
            idx += 1
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


print(sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]))
#expected output: [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
print('---------------------------------------')

print(sort_012([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]))
#expected output: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
print('---------------------------------------')

print(sort_012([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]))
#expected output: [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
print('---------------------------------------')

print(sort_012([]))
#expected output: []
test_function([])
print('---------------------------------------')

print(sort_012([0, 0, 0, 2, 0, 0, 2, 2, 0, 2, 2, 0]))
#expected output: [0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2]
test_function([0, 0, 0, 2, 0, 0, 2, 2, 0, 2, 2, 0])
print('---------------------------------------')

print(sort_012([1, 1, 1, 1, 1, 1]))
#expected output: [1, 1, 1, 1, 1, 1]
test_function([1, 1, 1, 1, 1, 1])
print('---------------------------------------')

