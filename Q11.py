### Question 11 ### 
'''
Write a function to generate checksums (MD5sum) of files contained within a given direcroy. You must use the os module to generate the checksums.  
The function must accept a path to an input directory (as a string), calculate the checksums and save the checksums generated to a new file.

'''


import os   
import subprocess

from pathlib import Path

def check(input_directory):
    p = Path(input_directory)
    files = list(p.glob("*")) 
    md5file=""
    for file in files:
        task = subprocess.Popen(['md5sum',file],
                                stdin = subprocess.PIPE,
                                stdout = subprocess.PIPE,
                                stderr = subprocess.PIPE
                                )
        (out, err)=task.communicate()
        out_string=out.decode("utf-8") 
        err_msg=err.decode("utf-8")
        if err_msg:
            print(err_msg)
        md5file+=out_string
    print(md5file)
    with open("output.txt", "a+") as o_file:
        o_file.write(md5file)

check('./S-BG-S2-Mathew/')
#Comment and add a write out to the directory file. 

