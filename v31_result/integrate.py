import os

aaa = 'v31PDR_all.result'
a = ['v31PDRTem2','v31PDRTem3','v31PDRTem4','v31PDRTem5',
     'v31PDRTem7','v31PDRTem9']
b = '_all.result'

f = open(aaa,'r')
g = open('all.csv','w')

ff_all = []
os.system('wc '+aaa+' -l')
for c in a:
  os.system('wc '+c+b+' -l')
  ff_all.append(open(c+b,'r').readlines())

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
