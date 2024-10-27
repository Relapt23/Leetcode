# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

def defangIPaddr(address: str):
    ans = []
    for elem in address:
        if elem == ".":
            ans.append("[.]")
            continue
        ans.append(elem)
    return ''.join(map(str, ans))

print(defangIPaddr("1.1.1.1"))