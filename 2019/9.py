values = [int(l.strip()) for l in "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99".split(",")]
values = [int(l.strip()) for l in "1102,34915192,34915192,7,4,7,99,0".split(",")]
values = [int(l.strip()) for l in "104,1125899906842624,99".split(",")]
values = [int(l.strip()) for l in open("9.txt").readline().split(",")]

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
        return self.output

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
c.add_input([2])
c.execute()
print(c.get_output()[0])
exit(0)
settings = [0,1,2,3,4]
possible = []
for a in settings:
    bpos = list(settings)
    bpos.remove(a)
    for b in bpos:
        cpos = list(bpos)
        cpos.remove(b)
        for c in cpos:
            dpos = list(cpos)
            dpos.remove(c)
            for d in dpos:
                epos = list(dpos)
                epos.remove(d)
                possible.append([a,b,c,d,epos[0]])

best = 0
best_comb = []
for pos in possible:
    output_value = 0
    for phase in pos:
        s = calc(memfactory())
        s.add_input([phase, output_value])
        s.execute()
        output_value = s.get_output()[0]        
    if best < output_value:
        best = output_value
        best_comb = pos
print(best, best_comb)
