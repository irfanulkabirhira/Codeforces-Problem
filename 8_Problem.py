import sys
input = sys.stdin.read

def solve():
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n, q = int(data[idx]), int(data[idx + 1])
        idx += 2
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        # Precompute prefix sums of the array a and its cyclic shifts.
        prefix_sum = [0] * (n * n + 1)
        b = [0] * (n * n)  # We are not actually constructing 'b'
        
        # Fill in prefix sums as if we are constructing 'b'
        for i in range(n):
            for j in range(n):
                b[i * n + j] = a[(i + j) % n]
        
        # Precompute prefix sum array for array b
        for i in range(1, n * n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + b[i - 1]
        
        # Process queries
        for _ in range(q):
            l, r = int(data[idx]), int(data[idx + 1])
            idx += 2
            results.append(prefix_sum[r] - prefix_sum[l - 1])
    
    sys.stdout.write("\n".join(map(str, results)) + "\n")

# Main function to trigger the solution
if __name__ == "__main__":
    solve()
