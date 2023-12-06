import random
pv =(random.randrange(10))
vt = {
1:(pv,0,0),
2:(0,pv,0),
3:(0,0,pv)
}
#print(vt[random.randrange(3)])
#print(random.randrange(3))
#print(vt[3])
print(random.choice(list(vt.keys())))
choice = random.choice(list(vt.keys()))
print(vt[choice])