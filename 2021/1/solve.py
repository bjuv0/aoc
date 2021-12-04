inp = list(map(int, [line for line in open("inp")]))
tot = 0
for i in range(len(inp)-1):
    if inp[i] < inp[i+1]:
        tot += 1
print(tot)

tot = 0
for i in range(len(inp)-3):
    if sum(inp[i:i+3]) < sum(inp[i+1:i+4]):
        tot += 1

print(tot)
