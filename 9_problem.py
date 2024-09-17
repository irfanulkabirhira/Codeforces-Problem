def klee_super_duper_large_array():
    t = int(input())  # Number of test cases
    for _ in range(t):
        n, k = map(int, input().split())
        if n % 2 == 0:
            print(n // 2)
        else:
            print((n - 1) // 2)

# Calling the function
klee_super_duper_large_array()
