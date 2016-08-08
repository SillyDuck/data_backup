for l in open('all2.csv','r'):
  l = l.split(',')
  if l[1] != 'timeout' and l[3] != 'at' and float(l[3]) <= 300.0:
    print l[0]+'.aig'
