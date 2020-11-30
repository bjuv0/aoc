inp = open("8.txt").readline().strip()
w = 25
h = 6
layersize = w*h
nr_of_layers = len(inp)//layersize
layers = []
best = 999999
bestlayer = ""
for layer in range(nr_of_layers):
    l = inp[:layersize]
    layers.append(l)
    inp = inp[layersize:]

    if l.count("0") < best:
        best = l.count("0")
        print("new best %s"%(l))
        bestlayer = l

print(bestlayer.count("1")*bestlayer.count("2"))
canvas = [" " for x in range(layersize)]
for layer in reversed(layers):
    for i in range(layersize):
        if layer[i] == "0":
            canvas[i]=" "
        elif layer[i] == "1":
            canvas[i]="#"

for x in range(h):
    print("".join(canvas[:w]))
    canvas = canvas[w:]
