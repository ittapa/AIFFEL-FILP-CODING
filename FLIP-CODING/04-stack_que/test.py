
AL= [[2, 1], [1, 0], [3, 0], [2, 1]]

NL = []
for a in AL:
    if a[1] == 0:
        NL.append(a[0])
print(max(NL))

a = max([a[0] for a in AL if a[1]==0])



print(a)
print(type(a))



