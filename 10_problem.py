def hira():
    p = int(input())  
    for _ in range(p):
        n = int(input())  
        points_y0 = {}
        points_y1 = {}
        
        for _ in range(n):
            x, y = map(int, input().split())
            if y == 0:
                if x in points_y0:
                    points_y0[x] += 1
                else:
                    points_y0[x] = 1
            else:
                if x in points_y1:
                    points_y1[x] += 1
                else:
                    points_y1[x] = 1
        
        count_y0 = len(points_y0)
        count_y1 = len(points_y1)
        
        result = count_y0 * count_y1
        print(result)

