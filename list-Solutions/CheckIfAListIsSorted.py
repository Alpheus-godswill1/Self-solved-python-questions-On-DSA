#  Check if a list is sorted in ascending order.
Value = [1,2,2,3,3,4,4,5,5,5]

if Value != Value.sort(): 
    print("List is not sorted")
    
if not Value.sort():
    print("List is not sorted")