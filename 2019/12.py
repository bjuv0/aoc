from math import gcd

class moon:
    def __init__(self, str):
        attr = {}
        for assign in str.split(","):
            parts = assign.strip().split("=")
            attr[parts[0]] = int(parts[1])
        self.x = attr["x"]
        self.y = attr["y"]
        self.z = attr["z"]
        self.vx = 0
        self.vy = 0
        self.vz = 0

    def __str__(self):
        return "x=%d y=%d z=%d       vx=%d vy=%d vz=%d"%(self.x, self.y, self.z, self.vx, self.vy, self.vz)

    def pot(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def kin(self):
        return abs(self.vx) + abs(self.vy) + abs(self.vz)


inp = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""

inp = """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""
moons = [moon(x.strip()[1:-1]) for x in inp.split("\n")]
moons = [moon(x.strip()[1:-1]) for x in open("12.txt").readlines()]

pairs = []
for x in moons:
    for y in moons:
        if x!=y and (x,y) not in pairs and (y,x) not in pairs:
            pairs.append((x,y))

print("################ 0")
for m in moons:
    print(m)
print()

xiter = {}
yiter = {}
ziter = {}

xfound = False
yfound = False
zfound = False

xrep = 0
yrep = 0
zrep = 0
for i in range(1000000000):
    for p in pairs:
        if p[0].x > p[1].x:
            p[0].vx -= 1
            p[1].vx += 1
        elif p[0].x < p[1].x:
            p[0].vx += 1
            p[1].vx -= 1

        if p[0].y > p[1].y:
            p[0].vy -= 1
            p[1].vy += 1
        elif p[0].y < p[1].y:
            p[0].vy += 1
            p[1].vy -= 1

        if p[0].z > p[1].z:
            p[0].vz -= 1
            p[1].vz += 1
        elif p[0].z < p[1].z:
            p[0].vz += 1
            p[1].vz -= 1

    
    for m in moons:
        m.x += m.vx
        m.y += m.vy
        m.z += m.vz

    if not xfound:
        xstate = (
            moons[0].x,
            moons[1].x,
            moons[2].x,
            moons[3].x,
            moons[0].vx,
            moons[1].vx,
            moons[2].vx,
            moons[3].vx
        )
        if xstate in xiter:
            xrep = i
            print("x found %d"%(xrep))
            xfound = True
        else:
            xiter[xstate] = i

    if not yfound:
        ystate = (
            moons[0].y,
            moons[1].y,
            moons[2].y,
            moons[3].y,
            moons[0].vy,
            moons[1].vy,
            moons[2].vy,
            moons[3].vy
        )
        if ystate in yiter:
            yrep = i
            print("y found %d"%(yrep))
            yfound = True
        else:
            yiter[ystate] = i

    if not zfound:
        zstate = (
            moons[0].z,
            moons[1].z,
            moons[2].z,
            moons[3].z,
            moons[0].vz,
            moons[1].vz,
            moons[2].vz,
            moons[3].vz
        )
        if zstate in ziter:
            zrep = i
            print("z found %d"%(zrep))
            zfound = True
        else:
            ziter[zstate] = i

    if xfound and yfound and zfound:
        break
    
    #print("################ %d"%(i+1))
    #for m in moons:
    #    print(m)
    #print()


#print(sum([m.kin()*m.pot() for m in moons]))
print(xrep, yrep, zrep)
xmul = 1
ymul = 1
zmul = 1
while(True):
    x = xrep*xmul
    y = yrep*ymul
    z = zrep*zmul
    if x == y:# and y == z:
        break
    if x < y:
        xmul+=1
#    elif x < z:
#        xmul+=1
    elif y < x:
        ymul+=1
#    elif y < z:
#        ymul+=1
#    elif z < x:
#        zmul+=1
#    elif z < y:
#        zmul+=1
print("xy found %d"%(x))
xyrep = x
xymul = 1
largezmul = (xyrep // z) - 1
largez = largezmul * zrep
print(largezmul, largez)
while(True):
    xy = xyrep*xymul
    z = zrep*zmul
    if xy == z:# and y == z:
        break
    if xy < z:
        xymul+=1
#    elif x < z:
#        xmul+=1
    elif z < xy:
        if (z + largez) < xy:
            zmul+=largezmul
        else:
            zmul+=1
#    elif y < z:
#        ymul+=1
#    elif z < x:
#        zmul+=1
#    elif z < y:
#        zmul+=1
        

print(xy)
