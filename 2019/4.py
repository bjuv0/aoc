lines = [l.strip() for l in open("4.txt").readlines()]

nrs = [int(x) for x in lines[0].split("-")]
print(nrs)

passwd = []
for x in range(nrs[0],nrs[1]+1):
    s = str(x)
    double = False
    cons = 0
    ok = False
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            if cons == 0:
                cons = 2
                double = True
                if i == len(s)-1 or s[i] != s[i+1]:
                    ok = True
            elif cons == 2 :
                cons = 3
        else:
            cons = 0
        if s[i] < s[i-1]:
            double = False
            break
    if double and ok:
        print(s)
        passwd.append(s)

print(len(passwd))
