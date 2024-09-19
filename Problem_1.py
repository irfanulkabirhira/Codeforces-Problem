def solve():
    vowels = "aeiou"  # Our base vowel string to cycle through
    t = int(input())  # Number of test cases
    for _ in range(t):
        n = int(input())  # Length of the string for each test case
        result = (vowels * ((n // 5) + 1))[:n]  # Cycle through "aeiou" and take first 'n' characters
        print(result)

# Read input and call the function
solve()
