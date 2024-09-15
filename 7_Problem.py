def solve():
    t = int(input())  # Number of test cases
    for _ in range(t):
        # Reading the values of n, k, and q
        n, k, q = map(int, input().split())
        # Reading the array a
        a = list(map(int, input().split()))
        
        # For each query, we need to compute the result
        for _ in range(q):
            l, r = map(int, input().split())
            # Adjust for 0-based index
            l -= 1
            r = l + k - 1
            subarray = a[l:r+1]

            # Count the minimum number of operations needed to make the subarray consecutive
            operations = 0
            for i in range(1, len(subarray)):
                if subarray[i] != subarray[i-1] + 1:
                    operations += 1
            
            print(operations)

# Calling the solve function to handle the input/output
solve()
