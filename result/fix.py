import sys
f = open(sys.argv[1],'r')

ff = f.readlines()
g = open('real'+sys.argv[1],'w')

i = 0
while i < len(ff):
    print ff[i]
    s = (ff[i]).split(',')
    if s[1] == 'SAT':
        g.write(ff[i][:-1])
        g.write(','+ff[i+1])
        i+=2
    else:
        g.write(ff[i])
        i+=1
