
am = ['ori', 'Tem2', 'Tem3']#, 'Tem4', 'Tem5', 'Tem7', 'Tem9']
an = list()
al = list()
al2 = list()
vbvb = list()
for l in am:
  al.append(list())
  al2.append(list())

f = open('v30.csv','r')
ff = f.readlines()

at = list()
at2 = list()
#fast_case = []
redo_case = set()

p = open('v31.csv','r')
pp = p.readlines()

ms = open('multi.csv','r')
msms = ms.readlines()


q = open('v3sTranSigDetect.result','r')
qq = q.readlines()

q2 = open('v3sPDRDeepTem.result','r')
qq2 = q2.readlines()

q3 = open('v3sPDRFWDRC.result','r')
qq3 = q3.readlines()

q4 = open('v3sPDRTSS.result','r')
qq4 = q4.readlines()

runtime_dict = dict()

def preprocess(hh,alltype,alldata):
  for g in range(len(hh)):
    alltype.append("UNKNOWN")
  for g,l in enumerate(hh):
    l = l.strip().split(',')
    if l[3] == '':
      runtime_dict[l[0]] = 900.0
    elif l[3] =='at':
      runtime_dict[l[0]] = 0.99
    else:
      runtime_dict[l[0]] = float(l[3])
    for i,k in enumerate(alldata):
      if l[3+i*3] == '':
          k.append(900.0)
      elif l[3+i*3] == 'at':
          k.append(0.99)
          redo_case.add(l[0])
      else :
          k.append(float(l[3+i*3]))
      if l[1+i*3] == "SAT":
        alltype[g] = "SAT"
        continue
      elif l[1+i*3] == "UNSAT":
        alltype[g] = "UNSAT"
        continue

#opop = open('fast_caseList','w')
#for l in fast_case:
#  opop.write(l+'.aig\n')

def overviews(alltype,alldata):
  al2.append(list())
  vb_proved = 0
  vb_disproved = 0
  notsolvedbyorigin = 0
  unsolve_only = []
  gg_only= []
  solve_only = []
  total_proved =[]
  total_disproved = []
  total_solved = []
  avg = []
  avgc = []
  cc = 0.0
  vb_min = 0.0
  vb_min2 = 0.0
  for l in range(len(alldata)-1):
    solve_only.append(0)
    unsolve_only.append(0)
    gg_only.append(0)
    total_proved.append(0)
    total_disproved.append(0)
    total_solved.append(0)
    avg.append(0.0)
    avgc.append(0.0)

  for i in range(len(alldata[0])):
    n900 = 0
    idx = -1
    y900 = 0
    idx2 = -1
    mint = 900.0
    for j,l in enumerate(alldata):
      if j >= len(alldata)-1: break
      if l[i] != 900.0:
        if alldata[0][i] == 900.0:
          gg_only[j] +=1
        if l[i] < mint:
          mint = l[i]
        n900 += 1
        idx = j
        if alltype[i] == 'SAT':
          total_disproved[j] += 1
        elif alltype[i] == 'UNSAT':
          total_proved[j] += 1
        total_solved[j] += 1
        avg[j] += l[i]
      if l[i] == 900.0:
        y900 += 1
        idx2 = j
    for j in range(len(alldata)-1):
      if alltype[i] == 'SAT':
        vb_disproved +=1
        break
      elif alltype[i] == 'UNSAT':
        vb_proved +=1
        break
    if n900 == 1:
      #if alldata[-1][i] != 900.0:
      #  print ff[i].split(',')[0] , alldata[-1][i]
      solve_only[idx] +=1
    if y900 == 1:
      unsolve_only[idx2] +=1
    if n900 == len(alldata)-1:
      for j in range(len(alldata)-1):
        avgc[j] += alldata[j][i]
        #print alldata[j][i]
      cc += 1.0
      vb_min2 += mint
    if alldata[0][i] == 900.0:
      if n900 >=1:
        notsolvedbyorigin += 1
    if mint != 900.0:
      vb_min += mint
    alldata[-1].append(mint)
  for i,l in enumerate(avgc):
    #if cc != 0:
    avgc[i] = l/cc
  for i,l in enumerate(avg):
    avg[i] = l/total_solved[i]
  #avg[0] = (avg[0]*total_solved[0] - 895.0)/(total_solved[0]-1)
  print "avg time",avg
  print "solve_only",solve_only
  print "GG", gg_only
  print "notsolvedbyorigin",notsolvedbyorigin
  print "unsolve_only",unsolve_only
  print "total_proved",total_proved
  print "total_disproved",total_disproved
  print "total_solved",total_solved
  print "vb_proved", vb_proved
  print "vb_disproved", vb_disproved
  print avgc
  print vb_min/470.0
  print vb_min2/cc
def cal_unsafe_cases(hh,alldata):

  for iii in range(2,3):#range(len(am)):
    aaa = 0.0
    bbb = 0.0
    rat = 0.0
    n = 0.0
    for i in range(len(alldata[0])):
      l = hh[i].strip().split(',')
      #if alldata[0][i] <= 10.0:
      #  fast_case.append(l[0])
      if ( l[1] == 'UNSAT' or l[1] == 'SAT' )and alldata[0][i] != 900.0:
        if alldata[iii][i] != 900.0 and alldata[0][i] <= 200.0 and alldata[iii][i] <= 200.0:
          #and alldata[0][i] >= 10.0 and alldata[iii][i] >= 10.0:
          if alldata[0][i]/alldata[iii][i] >= 1.0:
            print l[0] + '.aig'
            #print l[0]+','+str(alldata[0][i])+','+str(alldata[iii][i])+','+str(alldata[0][i]/alldata[iii][i])
          n+=1.0
          aaa+= alldata[0][i]
          bbb+= alldata[iii][i]
          rat += (alldata[0][i]/alldata[iii][i])
    #print aaa,bbb,rat/n

def accumulate(alldata):
  accu=[]

  for j in range(len(am)+1):
    accu.append(list())
    for t in range(0,900,10):
      accu[j].append(0)
      for i in range(len(alldata[0])):
        if alldata[j][i] <= float(t)+9.9:
          accu[j][-1] += 1
  g = open('accu_multi.csv','w')
  for t in range(len(accu[0])):
    g.write(str(t*10+10))
    for j in range(len(am)+1):
      g.write(','+str(accu[j][t]))
    g.write('\n')

def compare(alldata,alldata2):
  common_solved = 0
  common_solve_time_a = 0.0
  common_solve_time_b = 0.0
  common_solve_ratio = 0.0
  m = 2
  for i in range(len(alldata[0])):
    #if alldata[m][i] == 900.0 and alldata2[m][i] != 900.0:
    #  print "v30 not solved:",ff[i].strip().split(',')[0], "time : " , alldata2[m][i]
    if alldata2[0][i] == 900.0 and alldata2[m][i] != 900.0:
      #print "v31 origin not solved:",ff[i].strip().split(',')[0], "time : " , alldata2[m][i]
      pass
    if alldata2[m][i] == 900.0 and alldata2[0][i] != 900.0:
      #print "v31 tem2 not solved:",ff[i].strip().split(',')[0], "time : " , alldata2[0][i]
      pass
    if alldata2[m][i] != 900.0 and alldata2[0][i] != 900.0 and alldata2[m][i] >= 10.0 and alldata2[0][i] >= 10.0:
      print alldata2[0][i], alldata2[m][i], alldata2[0][i]/alldata2[m][i]
      common_solved += 1
      common_solve_time_a += alldata2[0][i]
      common_solve_time_b += alldata2[m][i]
      common_solve_ratio += alldata2[0][i]/alldata2[m][i]
  print common_solve_time_a, common_solve_time_b, str(common_solve_ratio/common_solved)

def tsdetect():
  #hahaha = open('TScaseList2','w')
  for i in range(len(al2[0])):
    l = qq[i].strip().split(',')
    if l[1] == 'error:-6':
      pass
    #elif float(l[1])/float(l[2]) >= 1.0/50.0 and l[3] != "0" and al2[0][i] >= 10.0 and int(l[3]) <= 50:
    elif l[3] != "0" and l[1] != '0':
      print l[0], l[1], l[2], l[3], al2[0][i], at2[i]
      #hahaha.write(l[0]+'.aig\n')
  pass

def deep_FWDRC():
  al2.append(list())
  # al2.append(list())
  # at2.append(list())
  at2.append(list())
  for i in range(len(al2[0])):
    # l = qq2[i].strip().split(',')
    # if l[1] == 'timeout':
    #   al2[-2].append(900.0)
    #   at2[-2].append('UNKNOWN')
    # elif l[5] == '0.000000':
    #   al2[-2].append(float(l[3]))
    #   at2[-2].append('SAT')
    # else:
    #   al2[-2].append(float(l[4]))
    #   at2[-2].append(l[2])
    l = qq3[i].strip().split(',')
    if l[1] == 'timeout' or l[1] == 'error:-6':
      al2[-1].append(900.0)
      at2[-1].append('UNKNOWN')
    else:
      al2[-1].append(float(l[3]))
      at2[-1].append(l[1])
  pass

def tss():
  a = 0.0
  b = 0.0
  unsolve_cases = 0
  orz = 0.0
  c = 0.0
  for i in range(len(qq4)):
    l = qq4[i].strip().split(',')
    if runtime_dict[l[0]] == 900.0 and l[4] != '':
      unsolve_cases+=1
      print l[0] +',timeout,' + l[4] +',' + l[1]
    else:
      if l[4] != '':# and int(l[1]) <= 20:
        print l[0] +','+ str(runtime_dict[l[0]]) +','+ l[4] +','+ l[1] + ',' +str(runtime_dict[l[0]]/float(l[4]))
        a += runtime_dict[l[0]]
        b += float(l[4])
        orz += runtime_dict[l[0]]/float(l[4])
        c+=1
  #print a, b , orz/c, unsolve_cases
  pass
if __name__ == '__main__':
  #preprocess(ff,at,al)
  preprocess(pp,at2,al2)
  #preprocess(msms,at2,al2)
  #print runtime_dict
  deep_FWDRC()
  #overviews(at,al)
  overviews(at2,al2)
  #accumulate(al2)
  #compare(al,al2)
  #tss()
  #cal_unsafe_cases(msms,al2)
  #cal_unsafe_cases(pp,al2)
