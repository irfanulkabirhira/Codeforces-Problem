# Input two integers a and b
a, b = map(int, input().split())

# The total sum of the brothers' numbers is 1 + 2 + 3 = 6
# The missing brother's number is calculated as 6 - (a + b)
late_brother = 6 - (a + b)

# Output the result
print(late_brother)
