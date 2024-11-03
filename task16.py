# You are given an m x n integer grid accounts where accounts[i][j]
# is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank.
# Return the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their bank accounts. 
# The richest customer is the customer that has the maximum wealth.

def maximumWealth(accounts):
    res_array = []
    sum = 0
    for i in accounts:
        for j in i:
            sum += j
        res_array.append(sum)
        sum = 0
    return max(res_array)

print(maximumWealth([[1,5],[7,3],[3,5]]))