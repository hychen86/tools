import os
import sys
import subprocess
import glob
import shutil


def process_batch():
    
    #main_path = '/home/intact/Hongyu_workspace/p3_a1/'
    #main_path = '/home/intact/Hongyu_workspace/p3_a1/'
    main_path = '/media/seq/Work1/Hongyu_workspace/p3_a1/'
    
    "Get all directories in main_path"
    dir_list = os.listdir(main_path)
    
    for dir in dir_list:
        
        #print(dir[:10])
            
        if (dir[0] != 'p'):
            continue
        if (dir[10] != 'f'):
            continue
        #print(dir)

        os.chdir(main_path + dir) # change path to sample_path
        
        dir_list1 = os.listdir(main_path + dir)

        #print(dir_list1)

        #if len(dir_list1) = 7:
        #os.chdir(main_path + dir + 'annotate_results')

        try:
            os.chdir(main_path + dir + '/annotate_results')
            txt_list = glob.glob('*.txt') # get all fastq files in dir
            #print(txt_list)
            if 'Pseudoarachniotus_sp.clusters.txt' in txt_list:
                #print('yes')
                cmd = 'cp Pseudoarachniotus_sp.clusters.txt ' + main_path + dir[:10] + 'Pseudoarachniotus_sp.clusters.txt'
                subprocess.run(cmd, shell = True) 
        except Exception as ex:
            print(ex)  

        



process_batch()
                

