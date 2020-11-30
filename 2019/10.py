rows = [l.strip() for l in """.#..#
.....
#####
....#
...##""".split("\n")]

'''rows = [l.strip() for l in """......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####""".split("\n")]
'''

'''
rows = [l.strip() for l in """#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.""".split("\n")]
'''

rows = [l.strip() for l in open("10.txt").readlines()]

import math

class ast:
    def __init__(self, x ,y, r, a):
        self.x = x
        self.y = y
        self.r = r
        self.a = a
    def __str__(self):
        return "ast: x=%d y=%d r=%f a=%f"%(self.x, self.y, self.r, self.a)

    def __lt__(self,other):
        return self.a < other.a or (self.a == other.a and self.r < other.r)

print("\n".join(rows))
asts = {}
for y in range(len(rows)):
    for x in range(len(rows[y])):
        if rows[y][x] == "#":
            asts[(x,y)] = 0

for k in asts:
    angles = []
    for a in asts:
        if k != a:
            angle = math.atan2(a[0]-k[0],k[1]-a[1])
            if angle < 0:
                angle = math.pi*2 + angle
            if angle not in angles:
                angles.append(angle)
    asts[k] = len(angles)
    #print("angles for %s is %s"%(k , angles))


best_dist = max(asts.values())
pos = [x for x in asts if asts[x] == best_dist][0]
print()
print(best_dist, pos)

l = []
for k in asts:
    if k == pos:
        continue
    r = math.sqrt(abs(k[0]-pos[0])**2 + abs(k[1]-pos[1]))
    a = math.atan2(k[0]-pos[0],pos[1]-k[1])
    if a < 0:
        a = math.pi*2 + a

    l.append(ast(k[0],k[1],r,a))

a = -1.0
for i in range(200):
    match = None
    for ast in sorted(l):
        if ast.a > a:
            match = ast
            break
    if match == None:
        #wrap!
        match = sorted(l)[0]

    l.remove(match)
    a = match.a


print()
print(match)
print(match.x*100+match.y)
#print("\n".join([str(x) for x in asts]))
