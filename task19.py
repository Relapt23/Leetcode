# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

def runningSum(nums):
    ans = []
    sum = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            sum += nums[j]
            ans.append(sum)
        return ans

print(runningSum([1,2,3,4]))