inp = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L""".split("\n")
inp = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN""".split("\n")
inp = [l.strip() for l in open("6.txt").readlines()]

edges = {}
revert = {}
for l in inp:
    parts = l.split(")")
    edges[parts[1]] = parts[0]
    if not parts[0] in revert:
        revert[parts[0]] = []
    revert[parts[0]].append(parts[1])

root = None
for v in edges.values():
    if v not in edges:
        if root == None:
            root = v
        else:
            print(fail)

print("root=%s"%(root))

o = {}
def calc_depth(k, d):
    o[k] = d
    if k in revert:
        for r in revert[k]:
            calc_depth(r,d+1)

calc_depth(root, 0)
for k in o:
    print("%s: %d"%(k, o[k]))

print("total=%d"%(sum(o.values())))

youpath = ["YOU"]
while youpath[0] != root:
    youpath.insert(0,edges[youpath[0]])
sanpath = ["SAN"]
while sanpath[0] != root:
    sanpath.insert(0,edges[sanpath[0]])

print("->".join(sanpath))
print("->".join(youpath))
for i in range(len(sanpath)):
    if sanpath[i] != youpath[i]:
        print("->".join(sanpath[:i]))
        print(o["YOU"] + o["SAN"] - o[sanpath[i-1]]*2 - 2)
        break
