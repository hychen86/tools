import os 
import sys
import subprocess 

File1_path = '/home/seq/Hongyu_workspace/PSp3MiSeq1/'
File2_path = '/home/seq/Hongyu_workspace/PSp3MiSeq2/'
Miseq1 = os.listdir(File1_path)
Miseq2 = os.listdir(File2_path)
#print(Miseq1)
#print(Miseq2)


for x in Miseq1:
    cmd = 'cat ' + File1_path + x + ' ' + File2_path + x + ' > ' + x 
    if x in Miseq2:
        subprocess.run(cmd, shell = True)
    else:
        print(x)
