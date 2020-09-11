import os
import sys
import subprocess
import glob
import pandas as pd

#main_path = '/home/intact/Hongyu_workspace/P3-a2/Allcluster'
main_path = '/media/seq/Work1/Hongyu_workspace/p3_a1/'

os.chdir(main_path)
txt_list = glob.glob('*.txt')
#print(txt_list)

for txt in txt_list:
    txtfile = open("all_clusters.txt", "w")
    cmd1 = 'echo ' + txt[:9] + ' >> all_cluster.txt'
    cmd2 = 'cat ' + txt + ' >> all_cluster.txt'
    subprocess.run(cmd1, shell = True)
    subprocess.run(cmd2, shell = True)
