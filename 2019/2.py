values = [int(l.strip()) for l in open("2.txt").readline().split(",")]
#values = [int(x) for x in "1,1,1,4,99,5,6,0,99".split(",")]

def execute(v, n):
    mem = list(values)
    mem[1] = v
    mem[2] = n

    pos = 0
    while True:
        op = mem[pos]
        if op == 99:
            break
        val1 = mem[pos+1]
        val2 = mem[pos+2]
        res = mem[pos+3]
        if op == 1:
            mem[res] = mem[val1] + mem[val2]
        elif op == 2:
            mem[res] = mem[val1] * mem[val2]
        else:
            print("opps")

        pos+=4
    return mem[0]

print(execute(12,2))

for verb in range(100):
    for noun in range(100):
        if execute(noun, verb) == 19690720:
            print(noun*100+verb)


