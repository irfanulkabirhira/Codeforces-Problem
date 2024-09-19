def solve():
    t = int(input())  # Number of test cases
    for _ in range(t):
        # For each test case
        n, m, q = map(int, input().split())  # n = number of cells, m = number of teachers, q = number of queries (q=1 in this problem)
        teachers = list(map(int, input().split()))  # Teachers' positions
        david_position = int(input())  # David's position
        
        # Calculate the distances from David to each teacher
        dist1 = abs(teachers[0] - david_position)
        dist2 = abs(teachers[1] - david_position)
        
        # David will be caught by the closest teacher
        print(min(dist1, dist2))

# Read input and call the function
solve()
