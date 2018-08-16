"""
  Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

  For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
  Bonus: Can you do this in one pass?
"""

def sum_to_k(list, k):
    table = {}

    for elem in list:
        compliment = k - elem
        # Look up compliment in dictionary
        if compliment in table:
            return True
        else:
            table[elem] = compliment

    return False

if __name__ == '__main__':

    print('list = [10, 15, 3, 7], k = 17', "result={}".format(sum_to_k([10, 15, 3, 7], 17)))
    print('list = [10, 15, 3, 8, -1], k = 17', "result={}".format(sum_to_k([10, 15, 3, 8, -1], 9)))
    print('list = [10, 15, 3, 8, -1], k = 17', "result={}".format(sum_to_k([10, 15, 3, 8, -1], 7)))
    print('list = [10, 1, 31, 8, -11], k = 17', "result={}".format(sum_to_k([10, 1, 31, 8, -11], 7)))