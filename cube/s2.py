f = open('v3sMulPDRcubeAna_all.result','r')
ff =f.readlines()

g = open('v3sMulPDRcubeAna_all_ori.result','r')
gg = g.readlines()

a=0
b=0
for i,l in enumerate(ff):
  l = l.split(',')
  h = gg[i].split(',')
  if l[1] != 'error:-6' and h[1] != 'error:-6' and l[1] != '0' and l[1] != 'timeout' and h[1] != 'timeout':
    r = float(h[1])/float(l[1])
    if r > 1.0:
      a+=1
    elif r < 1.0:
      b+=1
    print l[0],l[1],h[1],r
print a,b
