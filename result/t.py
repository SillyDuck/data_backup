f = open('all.csv','r')
a = list()
b = list()

for l in f:
    l = l.split(',')
    if l[3] == '':
        a.append(900.0)
    else :
        a.append(float(l[3]))
    if l[6] == '\n':
        b.append(900.0)
    else :
        b.append(float(l[6]))

for k in range(150,950,50):
    print str(k)+','+str(sum(i < k for i in a) ) +','+str(sum(i < k for i in b) )

c = 0
cc = 0
for i in range(len(a)):
    if a[i] == 900.0 and b[i] < 900.0:
        c+=1
    elif a[i] < 900.0 and b[i] == 900.0:
        cc+=1
print "b unique:"+str(c)
print "a unique:"+str(cc)

c = 0.0
cc = 0.0
for i in range(len(a)):
    if b[i] < 900.0:
        c+=b[i]
    elif a[i] < 900.0:
        cc+=a[i]
print "b total time:"+str(c)
print "a total time:"+str(cc)

c = 0
cc = 0
for i in range(len(a)):
    if a[i] < b[i]:
        c+=1
    elif a[i] > b[i]:
        cc+=1
print "b longer than a:"+str(c)
print "a longer than b:"+str(cc)
