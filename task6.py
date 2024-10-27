# In the town of Digitville, there was a list of numbers called nums containing integers from 0 to n - 1. 
# Each number was supposed to appear exactly once in the list, however, two mischievous numbers sneaked in an additional time, 
# making the list longer than usual.

# As the town detective, your task is to find these two sneaky numbers. 
# Return an array of size two containing the two numbers (in any order), so peace can return to Digitville.

def getSneakyNumbers(nums):
    a= []
    ans = []
    for elem in nums:
        if elem in a:
            ans.append(elem)
        a.append(elem)
    return ans

print(getSneakyNumbers([0,1,1,0]))