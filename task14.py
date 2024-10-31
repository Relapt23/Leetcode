# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

def singleNumber(nums):
    a = []
    for elem in nums:
        if elem not in a:
            a.append(elem)
        else:
            a.remove(elem)
    return a[0]
        
print(singleNumber([4,1,2,1,2]))