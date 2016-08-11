import sys

f = open('v30.csv','r')
ff = f.readlines()

p = open('v31.csv','r')
pp = p.readlines()

q3 = open('v3sPDRFWDRC.result','r')
qq3 = q3.readlines()

ms = open('multi.csv','r')
msms = ms.readlines()


if sys.argv[1] == '10':
  t = open('TRY10_UNSAT.result','r')
else:
  t = open('TRY50_UNSAT.result','r')
tt = t.readlines()

result_dict = dict()

# for l in ff:
#   l = l.strip().split(',')
#   result_dict[l[0]] = l[1]


time_dict = dict()

iii = 9

for l in msms:
  l = l.strip().split(',')
  if l[iii] == '':
    time_dict[l[0]] = 900.0
  else:
    time_dict[l[0]] = float(l[iii])
#print time_dict


def ver():
  for l in qq3:
    l = l.strip().split(',')
    if time_dict[l[0]] != 'timeout':
      if l[1] == 'SAT' and time_dict[l[0]] == 'UNSAT':
        print l[0]
      elif l[1] == 'UNSAT' and time_dict[l[0]] == 'SAT':
        print l[0]

def compare():
  a = 0.0
  b = 0.0
  c=0
  for l in tt:
    l = l.strip().split(',')
    if l[3] != '':
      print l[0], time_dict[l[0]], l[3] , time_dict[l[0]]/float(l[3])
      a += time_dict[l[0]]
      b += float(l[3])
    else:
      print l[0],time_dict[l[0]], "timeout"
      c+=1
  print a, b , c

compare()
