# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.

def smallerNumbersThanCurrent(nums):
    array = nums
    ans = []
    count = 0
    for i in range(len(nums)):
        for j in range(len(array)):
            if nums[i] > array[j]:
                count += 1
        ans.append(count)
        count = 0
    return ans


print(smallerNumbersThanCurrent([8,1,2,2,3]))