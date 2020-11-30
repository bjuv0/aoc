inp = """10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL""".split("\n")

inp = """9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL""".split("\n")

inp = """157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT""".split("\n")

inp = """2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF""".split("\n")

inp = [l for l in open("14.txt").readlines()]

ore_cargo = 1000000000000

class material:
    def __init__(self, str):
        p = str.strip().split(" ")
        self.name = p[1]
        self.amount = int(p[0])
        self.amount_needed = 0

    def __str__(self):
        return "%d %s"%(self.amount_needed, self.name)

class reaction:
    def __init__(self, str):
        p = str.split("=>")
        self.result = material(p[1])
        self.ingredients = []
        if len(p[0]) == 0:
            return
        for i in p[0].strip().split(","):
            self.ingredients.append(material(i))

    def __str__(self):
        return "%s"%(str(self.result))# <= %s"%(str(self.result), ", ".join([str(x) for x in self.ingredients]))

    def ore_count(self):
        return sum([x.amount_needed for x in self.ingredients if x.name == "ORE"])

reactions = {}
reactions["ORE"] = reaction("=> 1 ORE")
for l in inp:
    r = reaction(l)
    reactions[r.result.name] = r


def need(material, amount):
    #print("need %d %s"%(amount, material))
    r = reactions[material]
    r.result.amount_needed+=amount
    #print("  total need %d"%(r.result.amount_needed))
    conversions = r.result.amount_needed // r.result.amount
    if r.result.amount_needed % r.result.amount > 0:
        conversions+=1
    for ing in r.ingredients:
        new_need = ing.amount*conversions
        if ing.name != "ORE":
            delta = new_need - ing.amount_needed
            if delta > 0:
                need(ing.name,delta)
            
        ing.amount_needed = new_need

need("FUEL", 1)

def zero():
    for r  in reactions.values():
        r.result.amount_needed = 0
        for i in r.ingredients:
            i.amount_needed = 0

#for r in reactions.values():
#    print(r)

def get_ores():
    return sum([x.ore_count() for x in reactions.values()])

print(get_ores())

mino = 1
maxo = 100000000

while(True):
    zero()
    test_value = (mino+maxo)//2
    need("FUEL", test_value)
    ores = get_ores()
    print("%d ores gives %d fuel"%(ores, test_value))
    if ores > ore_cargo:
        maxo = test_value
    else:
        mino = test_value

    if abs(mino-maxo) == 1:
        break
    

exit(0)

mats = {}

for l in inp:
    parts = l.split("=>")
    m = parts[1].strip().split(" ")
    mat = m[1]
    amount = int(m[0])
    dep = []
    for ms in parts[0].strip().split(","):
        p = ms.strip().split(" ")
        dep.append((p[1],int(p[0])))
    if mat in mats:
        print("oppps!!!!")
        exit(0)
    mats[mat] = (amount, dep, mul)

def get_ore_count(count, mat):
    print("needs %d %s"%(count, mat))
    if mat == "ORE":
        return count
    if not mat in mats:
        print("Missing mats %s"%(mat))
        exit(0)
    amount_to_get = mats[mat][0]
    multiplier = 1
    if amount_to_get < count:
        multiplier = count // amount_to_get
        if count % amount_to_get > 0:
            multiplier += 1
    total_needed = 0
    for dep in mats[mat][1]:
        total_needed += get_ore_count(dep[1]*multiplier, dep[0])
    return total_needed



#print(get_ore_count(1, "FUEL"))

from collections import defaultdict

need = defaultdict(int)

def calc_need(count, mat):
    print("need %d %s"%(count, mat))
    need[mat] += count
    total_need = need[mat]
    print("  total need %d %s"%(total_need, mat))
    if mat == "ORE":
        return
    if not mat in mats:
        print("Missing mats %s"%(mat))
        exit(0)
    amount_to_get = mats[mat][0]
    multiplier = 1
    if amount_to_get < needed:
        multiplier = needed // amount_to_get
        if needed % amount_to_get > 0:
            multiplier += 1

    for dep in mats[mat][1]:
        calc_need(dep[1]*multiplier, dep[0])

#calc_need(1, "FUEL")

def calc_need2(amount, mat):
    # add need total
    need[mat] += amount
    if mat == "ORE":
        return
    for dep in mats[mat][1]:
        pass

calc_need2(1,"FUEL")

for n in need:
    print(n, need[n])
