# You are given two strings s and t such that every character occurs at most once in s and t is a permutation of s.

# The permutation difference between s and t is defined as the sum of the absolute difference between the index of the occurrence of each character in s and the index of the occurrence of the same character in t.

# Return the permutation difference between s and t.

def findPermutationDifference(s, t):
    array_s = []
    array_t = []
    sum = 0
    for elem in s:
        array_s.append(elem)
    for sym in t:
        array_t.append(sym)
    for i in range(len(array_s)):
        for j in range(len(array_t)):
            if array_s[i] == array_t[j]:
                sum += abs(i-j)
    return sum
print(findPermutationDifference("abcde","edbac"))