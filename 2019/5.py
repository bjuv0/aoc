values = [int(l.strip()) for l in open("5.txt").readline().split(",")]

input_value = 5
output_value = 0

def execute():
    global input_value
    global output_value
    mem = list(values)
    pos = 0
    while True:
        op = mem[pos]
        o = op%100
        m1 = (op//100)%10
        m2 = (op//1000)%10
        m3 = (op//10000)
        print("%s op=%d par1=%d par2=%d par3=%d"%(op, o, m1, m2, m3))
        if o == 1:
            print(mem[pos:pos+4])
            if m1 == 0:
                val1 = mem[mem[pos+1]]
            elif m1 == 1:
                val1 = mem[pos+1]                
            else:
                print("error m1 %d"%(m1))
                return
            if m2 == 0:
                val2 = mem[mem[pos+2]]
            elif m2 == 1:
                val2 = mem[pos+2]
            else:
                print("error m2")
                return
            if m3 != 0:
                print("error m3")
                return
            res = mem[pos+3]
            mem[res] = val1 + val2
            pos+=4
        elif o == 2:
            print(mem[pos:pos+4])
            if m1 == 0:
                val1 = mem[mem[pos+1]]
            elif m1 == 1:
                val1 = mem[pos+1]                
            else:
                print("error")
                return
            if m2 == 0:
                val2 = mem[mem[pos+2]]
            elif m2 == 1:
                val2 = mem[pos+2]
            else:
                print("error")
                return
            if m3 != 0:
                print("error")
                return
            res = mem[pos+3]
            mem[res] = val1 * val2
            pos+=4
        elif o == 3:
            print(mem[pos:pos+2])
            res = mem[pos+1]
            mem[res] = input_value
            pos+=2
        elif o == 4:
            print(mem[pos:pos+2])
            res = mem[pos+1]
            output_value = mem[res]
            pos+=2
        elif o == 5:
            print(mem[pos:pos+3])
            if m1 == 0:
                val1 = mem[mem[pos+1]]
            elif m1 == 1:
                val1 = mem[pos+1]                
            else:
                print("error m1 %d"%(m1))
                return
            if m2 == 0:
                val2 = mem[mem[pos+2]]
            elif m2 == 1:
                val2 = mem[pos+2]
            else:
                print("error m2")
                return
            if val1 != 0:
                pos = val2
            else:
                pos+=3
        elif o == 6:
            print(mem[pos:pos+3])
            if m1 == 0:
                val1 = mem[mem[pos+1]]
            elif m1 == 1:
                val1 = mem[pos+1]                
            else:
                print("error m1 %d"%(m1))
                return
            if m2 == 0:
                val2 = mem[mem[pos+2]]
            elif m2 == 1:
                val2 = mem[pos+2]
            else:
                print("error m2")
                return
            if val1 == 0:
                pos = val2
            else:
                pos+=3
        elif o == 7:
            print(mem[pos:pos+4])
            if m1 == 0:
                val1 = mem[mem[pos+1]]
            elif m1 == 1:
                val1 = mem[pos+1]                
            else:
                print("error")
                return
            if m2 == 0:
                val2 = mem[mem[pos+2]]
            elif m2 == 1:
                val2 = mem[pos+2]
            else:
                print("error")
                return
            if m3 != 0:
                print("error")
                return
            res = mem[pos+3]
            if val1 < val2:
                mem[res] = 1
            else:
                mem[res] = 0
            pos+=4
        elif o == 8:
            print(mem[pos:pos+4])
            if m1 == 0:
                val1 = mem[mem[pos+1]]
            elif m1 == 1:
                val1 = mem[pos+1]                
            else:
                print("error")
                return
            if m2 == 0:
                val2 = mem[mem[pos+2]]
            elif m2 == 1:
                val2 = mem[pos+2]
            else:
                print("error")
                return
            if m3 != 0:
                print("error")
                return
            res = mem[pos+3]
            if val1 == val2:
                mem[res] = 1
            else:
                mem[res] = 0
            pos+=4
        elif o == 99:
            return
        else:
            print("opps op=%d"%(op))
            return

execute()
print("output=%d"%(output_value))
