lines = [int(l.strip()) for l in open("1.txt").readlines()]

#for l in lines:
#    print(l)

def calc(x):
    f = (x//3)-2
    if f <= 0:
        return 0
#    print((x//3)-2)
    return f + calc(f)

print(calc(100756))

print(sum([calc(x) for x in lines]))
