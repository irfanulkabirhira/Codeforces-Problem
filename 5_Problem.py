def solve():
    t = int(input())  # Number of test cases
    for _ in range(t):
        # Read n, k, and q
        n, k, q = map(int, input().split())
        # Read array a
        a = list(map(int, input().split()))
        
        # Precompute f(b) for all subarrays of length k
        f = [0] * (n - k + 1)
        for i in range(n - k + 1):
            cnt = 0
            for j in range(i, i + k - 1):
                if a[j + 1] != a[j] + 1:
                    cnt += 1
            f[i] = cnt
        
        # Prefix sum for fast range queries
        prefix_sum = [0] * (n - k + 2)
        for i in range(1, n - k + 2):
            prefix_sum[i] = prefix_sum[i - 1] + f[i - 1]
        
        # Process queries
        for _ in range(q):
            l, r = map(int, input().split())
            l -= 1
            r -= 1
            # Sum f values from subarray starting at index l to r - k + 1
            result = prefix_sum[r - k + 2] - prefix_sum[l]
            print(result)

# Input and Output handling
solve()
