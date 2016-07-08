f = open('all.csv','r')
am = ['ori', 'Tem2', 'Tem3', 'Tem4', 'Tem5', 'Tem7', 'Tem9']
al = list()
at = list()
fast_case = []
for l in am:
  al.append(list())

redo_case = set()
ff = f.readlines()

for g in range(len(ff)):
  at.append("UNKNOWN")
for g,l in enumerate(ff):
  l = l.strip().split(',')
  for i,k in enumerate(al):
    if l[3+i*3] == '':
        k.append(900.0)
    elif l[3+i*3] == 'at':
        k.append(0.99)
        redo_case.add(l[0])
    else :
        k.append(float(l[3+i*3]))
    if l[1+i*3] == "SAT":
      at[g] = "SAT"
      continue
    elif l[1+i*3] == "UNSAT":
      at[g] = "UNSAT"
      continue

opop = open('fast_caseList','w')
for l in fast_case:
  opop.write(l+'.aig\n')

unsolve_only = []
solve_only = []
total_proved =[]
total_disproved = []
total_solved = []
avg = []
for l in am:
  solve_only.append(0)
  unsolve_only.append(0)
  total_proved.append(0)
  total_disproved.append(0)
  total_solved.append(0)
  avg.append(0.0)

for i in range(len(al[0])):
  n900 = 0
  idx = -1
  y900 = 0
  idx2 = -1
  for j,l in enumerate(al):
    if l[i] != 900.0:
      n900 += 1
      idx = j
      if at[i] == 'SAT':
        total_disproved[j] += 1
      elif at[i] == 'UNSAT':
        total_proved[j] += 1
      else:
        print ff[i].split(',')[0], at[i]
      total_solved[j] += 1
      avg[j] += l[i]
    if l[i] == 900.0:
      y900 += 1
      idx2 = j
  if n900 == 1:
    solve_only[idx] +=1
  if y900 == 1:
    unsolve_only[idx2] +=1
for i,l in enumerate(avg):
  avg[i] = l/total_solved[i]
print "avg time",avg
print "solve_only",solve_only
print "unsolve_only",unsolve_only
print "total_proved",total_proved
print "total_disproved",total_disproved
print "total_solved",total_solved

aaa = 0.0
bbb = 0.0
rat = 0.0
n = 0.0
iii = 2
for i in range(len(al[0])):
  l = ff[i].strip().split(',') 
  if al[0][i] <= 10.0:
    fast_case.append(l[0])
  if l[1] =='SAT' and al[0][i] != 900.0:
    if al[iii][i] != 900.0 and al[0][i] >= 10.0 and al[iii][i] >= 10.0:
      print l[0]+','+str(al[0][i])+','+str(al[iii][i])+','+str(al[0][i]/al[iii][i])
      n+=1.0
      aaa+= al[0][i]
      bbb+= al[iii][i]
      rat += (al[0][i]/al[iii][i])
print aaa,bbb,rat/n




t = range(0,900,10)
print t

accu=[]
for
#  for i in range(len(al[0])):
#    
#    for j,l in enumerate(al):
#      pass
