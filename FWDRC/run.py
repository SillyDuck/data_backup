import os
import sys
import subprocess
import threading
from subprocess import STDOUT, check_output

m_name = 'v3sPDRFWDRC'
script = 'ver pdr p1 -s\n'

class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None
    def run(self, timeout):
        def target():
            print 'Thread started'
            op = open(m_name+'caseResult.tmp','w')
            self.process = subprocess.Popen(self.cmd.split(), stdout=op)
            self.process.communicate()
            print 'Thread finished'
        thread = threading.Thread(target=target)
        thread.start()
        thread.join(timeout)
        if thread.is_alive():
            print 'Terminating process'
            self.process.terminate()
            thread.join()


print 'python run.py <caseList> \n'
f = open(sys.argv[1], 'r')
allcases = f.readlines()
result = open(m_name+'.result','w');
i = 1
for ll in allcases:
    cn = ll[:-5]
    print '\n\n\n'+m_name+'Running case : '+ cn + ' ,  '+str(i)+' / '+ str(len(allcases)) + '\n\n\n'
    i+=1
    w = open(m_name+'dofile.tmp', 'w')
    w.write( 'set solver -mi\n');
    w.write( 'read aig ../testcase/' + cn + '.aig\n');
    w.write( 'set safe 0\n' );
    w.write( script );
    w.write( 'q -f' );
    w.close();
    command = Command('./v3 -f '+m_name+'dofile.tmp');
    command.run(timeout=900)
    ret = command.process.returncode
    print "return code"
    print ret

    if(ret == -15):
        result.write(cn + ',timeout,,,,,,,,,,,,,,,,,,,,,\n')
    elif(ret != 0):
        result.write(cn + ',error:'+str(ret)+',,,,,,,,,,,,,,,,,,,,,\n')
    else:
        runtimeFile = open(m_name+'caseResult.tmp', 'r');
        rF_all = runtimeFile.readlines()
        for j,ggg in enumerate(rF_all):
            if ggg.startswith('Inductive'):
                aaa = ggg.split()
                result.write( cn+',' + 'UNSAT' + ',' + aaa[6] + ',' + aaa[9] + ',');
                for k in range(1,7):
                    bbb = rF_all[j+k].split()
                    if k ==4 or k ==5:
                        result.write( bbb[8] + bbb[11] + ',' + bbb[12][1:] + ',')
                    else:
                        result.write( bbb[9] + bbb[12] + ',' + bbb[13][1:] + ',')
                bbb = rF_all[j+7].split()
                result.write(bbb[-1][:-1]+'\n')
            elif ggg.startswith('Counter'):
                aaa = ggg.split()
                result.write( cn+',' + 'SAT' + ',' + aaa[5] + ',' + aaa[8] + ',');
                for k in range(1,7):
                    bbb = rF_all[j+k].split()
                    if k ==4 or k ==5:
                        result.write( bbb[8] + bbb[11] + ',' + bbb[12][1:] + ',')
                    else:
                        result.write( bbb[9] + bbb[12] + ',' + bbb[13][1:] + ',')
                bbb = rF_all[j+7].split()
                result.write(bbb[-1][:-1]+'\n')
            elif ggg.startswith('UNDECIDED'):
                result.write(cn + ',unknown,,,,,,,,,,,,,,,,,,,,,\n')


f.close()

