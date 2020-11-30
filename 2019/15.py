values = [int(l.strip()) for l in open("15.txt").readline().split(",")]

from collections import defaultdict
import msvcrt

def memfactory():
    global values
    d = defaultdict(int)
    for x in range(len(values)):
        d[x] = values[x]
    return d

class param:
    base = 0

    def __init__(self, calc, mode, pos):
        self.calc = calc
        self.mode = mode
        self.pos = pos

    def get(self):
        if self.mode == 0:
            return self.calc.mem[self.calc.mem[self.pos]]
        elif self.mode == 1:
            return self.calc.mem[self.pos]
        elif self.mode == 2:
            return self.calc.mem[param.base+self.calc.mem[self.pos]]
        else:
            print("error m1 %d"%(m1))
            return None
    
    def set(self, value):
        if self.mode == 0:
            res = self.calc.mem[self.pos]
        elif self.mode == 2:
            res = param.base+self.calc.mem[self.pos]
        else:
            print("error m3")
            return
        self.calc.mem[res] = value

class calc:
    def __init__(self, mem,inp=[]):
        self.mem = mem
        self.pos = 0
        self.inp = inp
        self.output = []

    def add_input(self, inp):
        self.inp.append(inp)

    def get_output(self):
        ret = self.output
        self.output = []
        return ret

    def dump_inst(self, n):
        str = ""
        for x in range(n):
            str += "%s "%(self.mem[self.pos+x])
        #print(str)

    def execute(self):
        while True:
            #time.sleep(1)
            op = self.mem[self.pos]
            o = op%100
            p1 = param(self, (op//100)%10, self.pos+1)
            p2 = param(self, (op//1000)%10, self.pos+2)
            p3 = param(self, (op//10000), self.pos+3)
            if o == 1:
                self.dump_inst(4)
                p3.set(p1.get() + p2.get())
                self.pos+=4
            elif o == 2:
                self.dump_inst(4)
                p3.set(p1.get() * p2.get())
                self.pos+=4
            elif o == 3:
                self.dump_inst(2)
                if (len(self.inp) == 0):
                    return 0
                p1.set(self.inp.pop(0))
                self.pos+=2
            elif o == 4:
                self.dump_inst(2)
                self.output.append(p1.get())
                self.pos+=2
            elif o == 5:
                self.dump_inst(3)
                if p1.get() != 0:
                    self.pos = p2.get()
                else:
                    self.pos+=3
            elif o == 6:
                self.dump_inst(3)
                if p1.get() == 0:
                    self.pos = p2.get()
                else:
                    self.pos+=3
            elif o == 7:
                self.dump_inst(4)
                if p1.get() < p2.get():
                    p3.set(1)
                else:
                    p3.set(0)
                self.pos+=4
            elif o == 8:
                self.dump_inst(4)
                if p1.get() == p2.get():
                    p3.set(1)
                else:
                    p3.set(0)
                self.pos+=4
            elif o == 9:
                self.dump_inst(2)
                param.base += p1.get()
                self.pos+=2
            elif o == 99:
                self.dump_inst(1)
                return -2
            else:
                print("opps op=%d"%(op))
                return -1

c = calc(memfactory())
d2i = {
    "n" : 1,
    "s" : 2,
    "w" : 3,
    "e" : 4
}

back = {
    "n" : "s",
    "s" : "n",
    "w" : "e",
    "e" : "w"
}

wall = 0
empty = 1
oxygen = 2

world = {}

def print_world(pos):
    maxx = -99999
    minx = 999999
    maxy = -999999
    miny = 999999
    
    for key in world:
        maxx = max(key[0],maxx)
        minx = min(key[0],minx)
        maxy = max(key[1],maxy)
        miny = min(key[1],miny)

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    #print("%d..%d, %d..%d"%(minx, maxx, miny,maxy))
    for y in range(maxy+1,miny-1,-1):
        str = ""
        for x in range(minx-1,maxx+1):
            if (x,y) == pos:
                str+="@"
                continue
            if not (x,y) in world:
                str+=" "
                continue
            if world[(x,y)] == 0:
                str+="#"
            if world[(x,y)] == 1:
                str+="."
            if world[(x,y)] == 2:
                str+="O"
        print(str)
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")


le_oxygen_distance = 9999999
oxygen_pos = None
def next_position(pos, dir):
    if dir == "n":
        return pos[0],pos[1]+1
    elif dir == "s":
        return pos[0],pos[1]-1
    elif dir == "w":
        return pos[0]-1,pos[1]
    elif dir== "e":
        return pos[0]+1,pos[1]
    

def search_from(pos, dir, depth):
    global le_oxygen_distance
    global oxygen_pos
    next_pos = next_position(pos, dir)

    c.add_input(d2i[dir])
    c.execute()
    output = c.get_output()

    if len(output) != 1:
        print("Unexpected output %s"%(output))
        exit(0)

    # update world 
    world[next_pos] = output[0]

    if output[0] == 0:
        return
    
    elif output[0] == 2:
        le_oxygen_distance = min(depth, le_oxygen_distance)
        oxygen_pos = next_pos
        
    for new_dir in d2i:
        candidate_position = next_position(next_pos, new_dir)
        if candidate_position not in world:
            search_from(next_pos, new_dir, depth+1)

    # move back
    c.add_input(d2i[back[dir]])
    c.execute()
    output = c.get_output() # assume open space

    #print_world(pos)

search_from((0,0), "e", 0)
print(le_oxygen_distance, oxygen_pos, sum([1 for x in world.values() if x == 0]))

oxy_queue = [oxygen_pos]
minutes = 0
while True:
    new_queue = []
    while len(oxy_queue) > 0:
        pos = oxy_queue.pop(0)
        world[pos] = 2
        for dir in d2i:
            next_pos = next_position(pos, dir)
            if world[next_pos] == 1:
                new_queue.append(next_pos)

    minutes+=1
    print_world(None)
    if len(new_queue) > 0:
        oxy_queue = new_queue
    else:
        break

print(minutes)

exit(0)
    
unexplored = {}
next_target = (0,1)
old_target = (0,1)
old_pos = (0,1)
stuck_count = 0

while True:
#for i in range(6):
    if d == "n":
        next_pos = (pos[0],pos[1]+1)
    elif d == "s":
        next_pos = (pos[0],pos[1]-1)
    elif d == "w":
        next_pos = (pos[0]-1,pos[1])
    elif d == "e":
        next_pos = (pos[0]+1,pos[1])
    else:
        print("Fail: d is %s"%(d))
        exit(0)

    # move in direction
    c.add_input(d2i[d])
    c.execute()
    output = c.get_output()

    if len(output) != 1:
        print("Unexpected output %s"%(output))
        exit(0)

    # update world 
    world[next_pos] = output[0]

    # move robot
    if output[0] > 0:
        #print("changing from %s to %s"%(pos, next_pos))
        pos = next_pos

    # goal reached?
    if output[0] == 2:
        break

    print_world(pos)

    rc = msvcrt.getch().decode("utf-8")
    if rc == "w":
        d = "n"
    if rc == "s":
        d = "s"
    if rc == "a":
        d = "w"
    if rc == "d":
        d = "e"

def bla():
    # explored new area?
    if next_pos in unexplored:
        del unexplored[next_pos]

    if not (pos[0],pos[0]+1) in world:
        unexplored[(pos[0],pos[0]+1)] = True
    if not (pos[0],pos[0]-1) in world:
        unexplored[(pos[0],pos[0]-1)] = True
    if not (pos[0]+1,pos[0]) in world:
        unexplored[(pos[0]+1,pos[0])] = True
    if not (pos[0]-1,pos[0]) in world:
        unexplored[(pos[0]-1,pos[0])] = True
        

    if next_target not in unexplored:
        next_target = next(iter(unexplored))

    xdelta = next_target[0]-pos[0]
    ydelta = next_target[1]-pos[1]
    print(xdelta, ydelta)
    if abs(xdelta) > abs(ydelta):
        if xdelta > 0:
            d = "e"
        else:
            d = "w"
    else:
        if ydelta > 0:
            d = "s"
        else:
            d = "n"

    print(next_target, pos)
    print(d)
    if pos == old_pos and old_target == next_target:
        stuck_count += 1
        if stuck_count > 3:
            print("STUCK!!!!")
            stuck_count = 0
            del unexplored[next_target]
            next_target = next(iter(unexplored))
            unexplored[old_target] = True


    old_target = next_target
    old_pos = pos
    
#print(world)
print(pos)

