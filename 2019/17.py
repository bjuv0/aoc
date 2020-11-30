values = [int(l.strip()) for l in open("17.txt").readline().split(",")]

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
c.execute()
output = c.get_output()
string = "".join([chr(x) for x in output])
print(string)

lines = string.strip().split("\n")
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] not in ["#", "."]:
            start_pos = (x,y)

d = "u"

rotate = {
     "u" : {
        "l" : "L",
        "r" : "R"
    },
     "d" : {
        "r" : "L",
        "l" : "R"
    },
    "l" : {
        "d" : "L",
        "u" : "R"
    },
    "r" : {
        "u" : "L",
        "d" : "R"
    }
}

def find_next_dir(pos, old_dir):
    global lines
    x = pos[0]
    y = pos[1]
    if old_dir in "ud":
        if x > 0  and lines[y][x-1] == "#":
            return "l"
        elif x <= len(lines[y]) and lines[y][x+1] == "#":
            return "r"
        else:
            return None
    elif old_dir in "lr":
        if y > 0  and lines[y-1][x] == "#":
            return "u"
        elif y <= len(lines) and lines[y+1][x] == "#":
            return "d"
        else:
            return None

        
def walk(pos, dir, depth=0):
    x = pos[0]
    y = pos[1]
    if dir == "l":
        if x == 0 or lines[y][x-1] == ".":
            return depth
        else:
            return walk((x-1,y),d,depth+1)
    elif dir == "r":
        if x == len(lines[y])-1 or lines[y][x+1] == ".":
            return depth
        else:
            return walk((x+1,y),d,depth+1)
    elif dir == "d":
        if y == len(lines)-1 or lines[y+1][x] == ".":
            return depth
        else:
            return walk((x,y+1),d,depth+1)
    elif dir == "u":
        if y == 0 or lines[y-1][x] == ".":
            return depth
        else:
            return walk((x,y-1),d,depth+1)


pos = start_pos
commands = []
while True:
    new_d = find_next_dir(pos,d)
    if new_d not in list("udlr"):
        break
    rotate_dir = rotate[d][new_d]
    commands.append(rotate_dir)
    d = new_d
    steps = walk(pos,d)

    if d == "l":
        pos = (pos[0]-steps,pos[1])
    elif d == "r":
        pos = (pos[0]+steps,pos[1])
    elif d == "u":
        pos = (pos[0],pos[1]-steps)
    elif d == "d":
        pos = (pos[0],pos[1]+steps)

    commands.append(str(steps))


A = ["L", "10", "L", "12", "R", "6"]
B = ["L", "10", "R", "10", "R", "6", "L", "4"]
C = ["R", "10", "L", "4", "L", "4", "L", "12"]
A = ",".join(A)
B = ",".join(B)
C = ",".join(C)

command = ",".join(commands)
command = command.replace(A,"A")
command = command.replace(B,"B")
command = command.replace(C,"C")
print("A = %s"%(A))
print("B = %s"%(B))
print("C = %s"%(C))
print(command)

c = calc(memfactory())
c.mem[0] = 2

print("pre exec")
c.execute()
output = c.get_output()
string = "".join([chr(x) for x in output])
print(string)

print("add main %s"%(command))
c.add_input([ord(x) for x in command+"\n"])
c.execute()
output = c.get_output()
string = "".join([chr(x) for x in output])
print(string)

print("add A %s"%(A))
c.add_input([ord(x) for x in A+"\n"])
c.execute()
output = c.get_output()
string = "".join([chr(x) for x in output])
print(string)

print("add B %s"%(B))
c.add_input([ord(x) for x in B+"\n"])
c.execute()
output = c.get_output()
string = "".join([chr(x) for x in output])
print(string)

print("add C %s"%(C))
c.add_input([ord(x) for x in C+"\n"])
c.execute()
output = c.get_output()
string = "".join([chr(x) for x in output])
print(string)

print("add response")
c.add_input([ord(x) for x in "n\n"])
c.execute()
output = c.get_output()
print(output)
string = "".join([chr(x) for x in output])
print(string)






exit(0)

c = calc(memfactory())
c.execute()
output = c.get_output()
string = "".join([chr(x) for x in output])
print(string)

lines = string.strip().split("\n")
#print(lines)
intersections = []
for y in range(1,len(lines)-1):
    for x in range(1,len(lines[y])-1):
        if (lines[y][x] == "#" and
            lines[y+1][x] == "#" and
            lines[y-1][x] == "#" and
            lines[y][x+1] == "#" and
            lines[y][x-1] == "#"):
            intersections.append((x,y))
print(intersections)
print(sum([i[0]*i[1] for i in intersections]))    
