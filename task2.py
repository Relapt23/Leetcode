# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

def numIdenticalPairs(nums):
    ans = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                ans += 1
    return ans
print(numIdenticalPairs([1,1,1,1]))