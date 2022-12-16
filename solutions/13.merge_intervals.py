def mergeIntervals(points):
    
   points.sort()
   count = 0


   while(count < len(points)):
    if(points[count][0] <= points[count + 1][0] and points[count][1] <= points[count + 1][1]):
        points[count] = [points[count][0], points[count + 1][1]]
        points.pop(count + 1)
         
    count += 1

    print(points)
        

mergeIntervals([[1,3],[2,6],[8,10],[15,18]])

