import os
import sys
import subprocess
import glob
import shutil
import pandas as pd 

main_path = '/media/seq/Work1/Hongyu_workspace/PSp3MiSeqcombine/'

os.chdir(main_path)
R1_list = glob.glob('*R1*.fastq.gz')
#R2_list = glob.glob('*R2*.fastq.gz')
R1_list.sort()
#R2_list.sort()  
#print(R1_list[:10])
#print(R2_list[:10])

'''sample_ls = []
for x in R1_list:
    sample_ls.append(x[:9])
print(sample_ls[8:16])'''

samples_ls = []
for R1 in R1_list:
    R2 = R1.replace('R1', 'R2')
    x = [R1, R2, R1[:9]]
    samples_ls.append(x)
#print (samples_ls[:6])

df = pd.DataFrame(samples_ls, columns = ['R1', 'R2', 'Sample'])
df.to_csv (r'/media/seq/Work1/Hongyu_workspace/PSp3MiSeqcombine/mappingfile.csv', index = False, header=True)