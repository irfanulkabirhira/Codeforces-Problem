def prefix_function(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

def solve():
    t = input().strip()
    n = len(t)
    
    # Calculate the prefix function for the string t
    pi = prefix_function(t)
    
    # The length of the largest prefix that is also a suffix
    overlap_length = pi[-1]
    
    # Check if the overlap is valid (it must be less than the length of t)
    if overlap_length == 0:
        print("NO")
        return
    
    # Possible message is the string before the overlap
    s = t[:n - overlap_length]
    
    # Validate by reconstructing the message
    if s + t[overlap_length:] == t:
        print("YES")
        print(s)
    else:
        print("NO")

# Call the function
solve()
