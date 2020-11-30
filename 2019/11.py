values = [int(l.strip()) for l in open("11.txt").readline().split(",")]

from collections import defaultdict

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
        self.inp.extend(inp)

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
c.add_input([1])
pos = (0,0)
d = "u"
lookup = {
    "u" : ["l", "r"],
    "d" : ["r", "l"],
    "l" : ["d", "u"],
    "r" : ["u", "d"]
}
panels = {}
while(True):
    ret = c.execute()
    if ret != 0:
        break
    out = c.get_output()
    #print(out)
    panels[pos] = out[0]
    d = lookup[d][out[1]]
    if d == "u":
        pos = (pos[0], pos[1] + 1)
    elif d == "d":
        pos = (pos[0], pos[1] - 1)
    elif d == "l":
        pos = (pos[0] + 1, pos[1])
    elif d == "r":
        pos = (pos[0] - 1, pos[1])
    else:
        print("Fail %s"%(d))
        break
    if pos in panels:
        c.add_input([panels[pos]])
    else:
        c.add_input([0])
    #print(pos, d)

print(len(panels))
maxx = 0
minx = 0
maxy = 0
miny = 0
for p in panels:
    print(panels[p])
    maxx = max(maxx,p[0])
    minx = min(minx,p[0])
    maxy = max(maxy,p[1])
    miny = min(miny,p[1])

print(maxx, minx, maxy, miny)

for y in range(-miny + 1):
    str = ""
    for x in range(-minx + 1):
        if (-x,-y) in panels and panels[(-x,-y)] == 1:
            str = str + "#"
        else:
            str = str + " "
    print(str)
            
