

def binary_search(values, target, high, low):
    if low > high:
        return False
    else: 
        mid = (low + high) // 2   # Pythonic approach - get Floor w/out math.floor
        if values[mid] == target:
            return True
        elif target < values[mid]:
            return binary_search(values, target, mid - 1, low)
        elif target > values[mid]:
            return binary_search(values, target, high, mid + 1)
        else:
            return False

if __name__ == '__main__':
    sorted_values = [1,3,4,5,7,8,18,23,34,65, 77,99, 105]
    target = 18
    print("List: " + str(sorted_values) )
    if binary_search(sorted_values, target, len(sorted_values)-1, 0):
        print("Target {} found in list".format(target))
    else:
        print("Target {} not in list".format(target))