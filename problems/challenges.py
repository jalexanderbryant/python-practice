
def sum_with_for(numbers):
  sum = 0
  for num in numbers:
    sum += num
  return sum

def sum_with_while(numbers):
  sum = 0
  i = 0
  while i < len(numbers):
    sum += numbers[i]
    i += 1
  return sum

def sum_with_recursion(numbers):
  
  # if base case=> numbers is empty
  if len(numbers) == 0:
  #   return 0
      return 0
  # if there are still numbers in list
  return numbers[0] + sum_with_recursion(numbers[1:])
  #   return numbers.head + sum_with_recursion(numbers[1:max])

def combine_alternate(list_a, list_b):
# Write a function that combines two lists by 
# alternatingly taking elements. 
# For example: given the two lists [a, b, c] and [1, 2, 3], 
# the function should return [a, 1, b, 2, c, 3].
  i = 0
  list_c = []
  while i < len(list_a):
    list_c.append(list_a[i])
    list_c.append(list_b[i])
    i += 1
  print(list_c)


def first_x_fibonacci(x=10):
  a = 0
  b = 1
  fibonacci_list = [a, b]
  while(len(fibonacci_list) != 10):
    c = a + b
    fibonacci_list.append(c)
    a = b
    b = c
    
  print(fibonacci_list)

def largest_number(input_list):
  # Write a function that given a list of non negative integers, 
  # arranges them such that they form the largest possible number. 
  # For example, given [50, 2, 1, 9], the largest formed number is 95021.

  # [50, 2, 1, 9]
  sort_for_largest = [str(x) for x in input_list]
  sort_for_largest.sort(reverse=True)
  largest = int(''.join(sort_for_largest))
  print(largest)


def sum_of_100():
  # Write a program that outputs all possibilities to put
  # + or - or nothing between the numbers 1, 2, ..., 9 (in this order)
  # such that the result is always 100. 
  # For example: 1 + 2 + 34 – 5 + 67 – 8 + 9 = 100.
  pass

def main():
  numbers = [1,2,3,4,5,6]
  # Problem 1
  # print(sum_with_for(numbers))
  print(sum_with_while(numbers))
  print(sum_with_recursion(numbers))

  # Problem 2
  # combine_alternate(['a', 'b', 'c'], [1,2,3])

  # Problem 3
  # first_x_fibonacci()

  # Problem 4
  # largest_number([50, 2, 1, 9])




if __name__ == '__main__':
  main()