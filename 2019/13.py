values = [int(l.strip()) for l in open("13.txt").readline().split(",")]

from collections import defaultdict
import msvcrt
import time

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
screen = {}
while(len(output) > 0):
    x = output.pop(0)
    y = output.pop(0)
    t = output.pop(0)
    screen[(x,y)] = t


print(len([x for x in screen.values() if x == 2]))


c = calc(memfactory())
c.mem[0] = 2
screen = {}
maxscore = 0
while(True):
    ret = c.execute()
    output = c.get_output()
    score = 0
    while(len(output) > 0):
        x = output.pop(0)
        y = output.pop(0)
        t = output.pop(0)
        if x == -1:
            score = t
            maxscore = max(maxscore, score)
        screen[(x,y)] = t
    x = 0
    y = 0
    canvas = []
    ball = None
    paddle = None
    while(True):
        if x == 0:
            canvas.append("")
        if (x,y) in screen:
            t = screen[(x,y)]
            if t == 0:
                canvas[y]+=" "
            elif t == 1:
                canvas[y]+="#"
            elif t == 2:
                canvas[y]+="+"
            elif t == 3:
                canvas[y]+="-"
                paddle = x
            elif t == 4:
                canvas[y]+="@"
                ball = x
            x+=1
        else:
            if (0,y) not in screen:
                break
            y+=1
            x = 0
    if ret == -2:
        break

    if paddle < ball:
        c.add_input([1])
    elif paddle > ball:
        c.add_input([-1])
    else:
        c.add_input([0])

  #  print(score)
    print("\n".join(canvas))
    time.sleep(0.001)

print("maxscore = %d"%(maxscore))
