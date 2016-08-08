f = open('all.csv','r')

a = set()
b = set()

for l in f :
  ll = l.split(',')[0]
  a.add(ll)
f.close()

g = open('Lowercase','r')

for l in g:
  ll = l.split(',')[0][0:-5]
  b.add(ll)
g.close()

for gg in b:
  if gg not in a:
    print gg
