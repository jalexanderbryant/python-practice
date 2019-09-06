
# Bubble Sort
# procedure bubblesort( A: list of sortable items)
def bubble_sort(items):
    swapped = True
#   repeat:
    while swapped == True:
#       swapped = false
        swapped = False 

#       for i = 1 to n-1 inclusive do
        curr = items.begin.next # Point to element just after header Sentinel
        while curr != items.end.prev: # Stop at node just be for trailer Sentinel 
#           /* if this pair is out of order */
#           if A[i-1] > A[1] then
            if curr.value > curr.next.value:
#               swap(A[i-1], A[i])
                curr.value, curr.next.value = curr.next.value, curr.value
#               swapped = true
                swapped = True
#           end if
            curr = curr.next
#       end for
#   until not swapped
# end procedure
