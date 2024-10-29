# Given an integer x, return true if x is a 
# palindrome, and false otherwise.

def isPalindrome(x):
    a1 =[]
    for elem in str(x):
        a1.append(elem)
    for i in range(len(a1)):
        if a1[::1] == a1[::-1]:
            continue
        else:
            return False
    return True
print(isPalindrome(-121))