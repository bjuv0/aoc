values=[int(x) for x in "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0".split(",")]
values=[int(x) for x in "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0".split(",")]
values=[int(x) for x in "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0".split(",")]
values=[int(x) for x in "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5".split(",")]
values=[int(x) for x in "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10".split(",")]
#values = [int(l.strip()) for l in open("7.txt").readline().split(",")]

import time

class calc:
    def __init__(self, mem,inp=[]):
        self.mem = mem
        self.pos = 0
        self.inp = inp

    def add_input(self, inp):
        self.inp.extend(inp)

    def get_output(self):
        return self.output
    
    def execute(self):
        while True:
            #time.sleep(1)
            op = self.mem[self.pos]
            o = op%100
            m1 = (op//100)%10
            m2 = (op//1000)%10
            m3 = (op//10000)
            #print("%s op=%d par1=%d par2=%d par3=%d"%(op, o, m1, m2, m3))
            if o == 1:
                #print(self.mem[self.pos:self.pos+4])
                if m1 == 0:
                    val1 = self.mem[self.mem[self.pos+1]]
                elif m1 == 1:
                    val1 = self.mem[self.pos+1]                
                else:
                    print("error m1 %d"%(m1))
                    return -1
                if m2 == 0:
                    val2 = self.mem[self.mem[self.pos+2]]
                elif m2 == 1:
                    val2 = self.mem[self.pos+2]
                else:
                    print("error m2")
                    return -1
                if m3 != 0:
                    print("error m3")
                    return -1
                res = self.mem[self.pos+3]
                self.mem[res] = val1 + val2
                self.pos+=4
            elif o == 2:
                #print(self.mem[self.pos:self.pos+4])
                if m1 == 0:
                    val1 = self.mem[self.mem[self.pos+1]]
                elif m1 == 1:
                    val1 = self.mem[self.pos+1]                
                else:
                    print("error")
                    return -1
                if m2 == 0:
                    val2 = self.mem[self.mem[self.pos+2]]
                elif m2 == 1:
                    val2 = self.mem[self.pos+2]
                else:
                    print("error")
                    return -1
                if m3 != 0:
                    print("error")
                    return -1
                res = self.mem[self.pos+3]
                self.mem[res] = val1 * val2
                self.pos+=4
            elif o == 3:
                #print(self.mem[self.pos:self.pos+2])
                res = self.mem[self.pos+1]
                if (len(self.inp) == 0):
                    return 0
                self.mem[res] = self.inp.pop(0)
                self.pos+=2
            elif o == 4:
                #print(self.mem[self.pos:self.pos+2])
                res = self.mem[self.pos+1]
                self.output = self.mem[res]
                self.pos+=2
            elif o == 5:
                #print(self.mem[self.pos:self.pos+3])
                if m1 == 0:
                    val1 = self.mem[self.mem[self.pos+1]]
                elif m1 == 1:
                    val1 = self.mem[self.pos+1]                
                else:
                    print("error m1 %d"%(m1))
                    return -1
                if m2 == 0:
                    val2 = self.mem[self.mem[self.pos+2]]
                elif m2 == 1:
                    val2 = self.mem[self.pos+2]
                else:
                    print("error m2")
                    return -1
                if val1 != 0:
                    self.pos = val2
                else:
                    self.pos+=3
            elif o == 6:
                #print(self.mem[self.pos:self.pos+3])
                if m1 == 0:
                    val1 = self.mem[self.mem[self.pos+1]]
                elif m1 == 1:
                    val1 = self.mem[self.pos+1]                
                else:
                    print("error m1 %d"%(m1))
                    return -1
                if m2 == 0:
                    val2 = self.mem[self.mem[self.pos+2]]
                elif m2 == 1:
                    val2 = self.mem[self.pos+2]
                else:
                    print("error m2")
                    return -1
                if val1 == 0:
                    self.pos = val2
                else:
                    self.pos+=3
            elif o == 7:
                #print(self.mem[self.pos:self.pos+4])
                if m1 == 0:
                    val1 = self.mem[self.mem[self.pos+1]]
                elif m1 == 1:
                    val1 = self.mem[self.pos+1]                
                else:
                    print("error")
                    return -1
                if m2 == 0:
                    val2 = self.mem[self.mem[self.pos+2]]
                elif m2 == 1:
                    val2 = self.mem[self.pos+2]
                else:
                    print("error")
                    return -1
                if m3 != 0:
                    print("error")
                    return -1
                res = self.mem[self.pos+3]
                if val1 < val2:
                    self.mem[res] = 1
                else:
                    self.mem[res] = 0
                self.pos+=4
            elif o == 8:
                #print(self.mem[self.pos:self.pos+4])
                if m1 == 0:
                    val1 = self.mem[self.mem[self.pos+1]]
                elif m1 == 1:
                    val1 = self.mem[self.pos+1]                
                else:
                    print("error")
                    return -1
                if m2 == 0:
                    val2 = self.mem[self.mem[self.pos+2]]
                elif m2 == 1:
                    val2 = self.mem[self.pos+2]
                else:
                    print("error")
                    return -1
                if m3 != 0:
                    print("error")
                    return -1
                res = self.mem[self.pos+3]
                if val1 == val2:
                    self.mem[res] = 1
                else:
                    self.mem[res] = 0
                self.pos+=4
            elif o == 99:
                return -2
            else:
                print("opps op=%d"%(op))
                return -1

#execute()
#print("output=%d"%(output_value))

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
    break
    output_value = 0
    for phase in pos:
        s = calc(list(values))
        s.add_input([phase, output_value])
        s.execute()
        output_value = s.get_output()        
    if best < output_value:
        best = output_value
        best_comb = pos
print(best, best_comb)

###################################### part 2
settings = [5,6,7,8,9]
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
mem = list(values)
for pos in possible:
    amps = [calc(list(values),[x]) for x in pos]
    next_input = 0
    while(True):
        for i in range(len(pos)):
            amps[i].add_input([next_input])
            ret = amps[i].execute()
            next_input = amps[i].get_output()
        if ret == -2:
            break
    if best < next_input:
        best = next_input
        best_comb = pos
print(best, best_comb)

