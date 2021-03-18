# Add more examples
def get_min_max(ints):
   """
   Return a tuple(min, max) out of list of unsorted integers.
   Args:
      ints(list): list of integers containing one or more integers
   """
   min_num = ints[0]
   max_num = ints[0]
   for i in ints:
      if i <min_num:
         min_num = i
      elif i >max_num:
         max_num = i
   return (min_num, max_num)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print(get_min_max(l))
# expected output:(0, 9)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print('---------------------------------------')

print(get_min_max([-2]))
# expected output:(-2, -2)
print ("Pass" if ((-2, -2) == get_min_max([-2])) else "Fail")
print('---------------------------------------')

print(get_min_max([0, 28, -7, 90, 15 ,150, -15]))
# expected output:(-15, 150)
print ("Pass" if ((-15, 150) == get_min_max([0, 28, -7, 90, 15 ,150, -15])) else "Fail")
print('---------------------------------------')

print(get_min_max([7,7,7,7,2]))
# expected output:(2, 7)
print ("Pass" if ((2, 7) == get_min_max([7,7,7,7,2])) else "Fail")
print('---------------------------------------')

print(get_min_max([-2,-18,-5,0,-32]))
# expected output:(-32, 0)
print ("Pass" if ((-32, 0) == get_min_max([-2,-18,-5,0,-32])) else "Fail")
print('---------------------------------------')


