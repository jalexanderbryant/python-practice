
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

def sum_with_recursion(numbers, pos):
  pass

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

def main():
  numbers = [1,2,3,4,5,6]
  # Problem 1
  print(sum_with_for(numbers))
  print(sum_with_while(numbers))
  

  # Problem 2
  combine_alternate(['a', 'b', 'c'], [1,2,3])

  # Problem 3
  first_x_fibonacci()



if __name__ == '__main__':
  main()