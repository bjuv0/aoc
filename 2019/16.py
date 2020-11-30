
inp = "12345678"
inp = "80871224585914546619083218645595"
inp = "19617804207202209144916044189917"
inp = "69317163492948606335995924319873"
#inp = "03036732577212944063491565474664"

inp = open("16.txt").readline().strip()

#print(inp)

message_offset = int(inp[:7])

block = [int(x) for x in inp]

def phase(block):
    new_block = [0]*len(block)
    for i in range(len(block)):
        pos = sum([block[ix-1] for ix in range(len(block)+1) if (ix // (i+1)%4) == 1])
        neg = sum([-block[ix-1] for ix in range(len(block)+1) if (ix // (i+1)%4) == 3])
        new_block[i] = abs((pos+neg))%10
    return new_block

#for i in range(8):
#    for ix in range(len(block)+1):
#        if (ix // (i+1)%4) == 1:
#            print(ix-1)
#    print("##########")
#exit(0)

for i in range(100):
    print(i)
    block = phase(block)
print(block)
print("".join([str(x)for x in block[:8]]))

exit(0)

def getpattern_and_index(iteration):
    base = [0,1,0,-1]
    counter = 0
    while True:
        counter+=1
        index = counter//(iteration+1)%len(base)
        yield counter-1, base[index]

def phase(string):
    new_string = [""]*len(string)
    for iteration in range(len(string)):
        sum = 0
        for i,p in getpattern_and_index(iteration):
            if i == len(string):
                break
            digit = int(string[i])
            #print(digit, p, (digit*p))
            sum += (digit*p)
        #print("    " ,iteration, sum)
        new_string[iteration] = str(abs(sum)%10)
    return new_string

string = list(inp)
for i in range(100):
    print(i)
    string = phase(string)
print(string)
print("".join(string[:8]))
print("".join(string[message_offset:message_offset+8]))
exit(0)

count = 0
for i,p in getpattern_and_index(2):
    count += 1
    if count > 10:
        break
    print(i,p)
