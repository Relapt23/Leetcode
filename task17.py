# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

def longestCommonPrefix(strs):
    ans = set()
    for str in strs:
        for elem in str:
            ans.add(elem)
    return ans

print(longestCommonPrefix(["flower","flow","flight"]))