import sys


if sys.argv[1] == '1':
  f = open('v31PDR_all.result','r')
else:
  f = open('v31PDRTem'+sys.argv[1]+'_all.result','r')
ff = f.readlines()

ss = ['SVR SOLVE','BMC SOLVE','GENERAL','PROPAGATE','TER SIM']

for i in range(5):
  avg = 0.0
  c=0
  for l in ff:
    ll = l.split(',')[9+i*3]
    if ll != '' and ll != '0.000000':
      c+=1
      avg+=float(ll)
  print ss[i]+" : ", avg/float(c)

