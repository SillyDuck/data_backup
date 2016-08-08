import os

aaa = 'v3sPDRMS_Upper.result'
aa = 'v3sPDRMS' 
a = ['2','3','4','5','7','9']
b = '_Upper.result'

f = open(aaa,'r')
g = open('all2.csv','w')

ff_all = []
os.system('wc '+aaa+' -l')
for c in a:
  os.system('wc '+aa+c+b+' -l')
  ff_all.append(open(aa+c+b,'r').readlines())

i = 0
for l in f:
  ll=l.split(',')
  g.write(ll[0]+','+ll[1]+','+ll[2]+','+ll[3])
  for cc in range(len(a)):
    e = ff_all[cc][i]
    ee = e.split(',')
    g.write(','+ee[1]+','+ee[2]+','+ee[3])
  i+=1
  g.write('\n')
