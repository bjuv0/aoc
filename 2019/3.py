lines = [l.strip() for l in open("3.txt").readlines()]
#lines = ["R8,U5,L5,D3", "U7,R6,D4,L4"]
#lines = ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]
#lines = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]
l1 = lines[0].split(",")
l2 = lines[1].split(",")

points = {}
x = 0
y = 0
sum = 0
points[(x,y)] = 0

for d in l1:
    dir = d[0]
    dist = int(d[1:])
    for z in range(dist):
        if dir == "R":
            x+=1
        elif dir == "L":
            x-=1
        elif dir == "U":
            y+=1
        elif dir == "D":
            y-=1
        if not (x,y) in points:
            points[(x,y)] = sum+z+1
    sum+=dist

x = 0
y = 0
sum = 0
mindist = 99999999999
i = 0
for d in l2:
    i+=1
    print("%d / %d"%(i,len(l2)))
    dir = d[0]
    dist = int(d[1:])
    for z in range(dist):
        if dir == "R":
            x+=1
        elif dir == "L":
            x-=1
        elif dir == "U":
            y+=1
        elif dir == "D":
            y-=1
        if (x,y) in points:
            print("Intersection at x=%d y=%d"%(x,y))
            #md = abs(x) + abs(y)
            md = points[(x,y)] + sum + z + 1
            print("   %d %d"%(points[(x,y)], sum + z + 1))
            if md < mindist:
                mindist = md
    sum+=dist
print("shortest distance = %d"%(mindist))




