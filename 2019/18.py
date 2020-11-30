inp="""#########
#b.A.@.a#
#########""".split("\n")

#inp="""########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################""".split("\n")

#inp=open("18.txt").readlines()
lines = [x.strip() for x in inp]
print("\n".join(lines))

import sys
sys.setrecursionlimit(15000)

specials = {}

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] not in "#.":
            specials[lines[y][x]] = (x,y)

all_doors = [x for x in specials if x >= "A" and x <= "X"]
all_keys = [x for x in specials if x >= "a" and x <= "x"]

for k in specials:
    print("%s = %s"%(k, specials[k]))

print("doors = %s"%(",".join(all_doors)))
print("keys = %s"%(",".join(all_keys)))

def neighbours(x,y):
    yield x+1,y
    yield x-1,y
    yield x,y+1
    yield x,y-1

adj = {x : {} for x in specials}

def search_shortest(org, x, y, points, depth=0):

    if (x,y) in points:
        if points[(x,y)] <= depth:
            return
    else:
        points[(x,y)] = depth
        
    for nx,ny in neighbours(x,y):
        c = lines[ny][nx] 
        if c == "#":
            continue
        elif c in specials and c != org:
            print("found x")
            return
        else:
            search_shortest

for x in adj:
    pos = specials[x]
    search_shortest(x, pos[0],pos[1],{})
    print("%s => %s"%(x,adj[x]))

exit(0)
    
best_path = 99999999
closest = {x : best_path for x in all_doors}
def explore(x, y, points, keys, open_doors, depth=0):
    global best_path
    #print(x,y, keys)
    if depth > best_path:
        return
    if set(all_keys) == set(keys):
        print("Found all keys at %d"%(depth))
        best_path = min(best_path, depth)
        return
    if (x,y) in points:
        if points[(x,y)] <= depth:
            return
    else:
        points[(x,y)] = depth

    for nx,ny in neighbours(x,y):
        c = lines[ny][nx] 
        if c == "#":
            continue
        elif c in all_keys and c not in keys:
            print("found key %s %s"%(c, keys))
            explore(nx,ny,{},keys+[c],open_doors,depth+1)
        elif c in all_doors and not c in open_doors:
            if not c.lower() in keys:
                continue
            # door reached
            if depth+1 >= closest[c]:
                continue
            print("reached door %s at %d"%(c,depth+1))
            closest[c] = depth+1
            explore(nx, ny, points, keys, open_doors+[c], depth+1)
        else:
            explore(nx, ny, points, keys, open_doors, depth+1)

start = specials["@"]
explore(start[0], start[1], {}, [], [])
print(best_path)
