### Question 3 ### 
'''

Write a script to remove all the duplicate lines from a text file (Gene_RD_rpt.txt).
Note- you may need to recreate the input file each time this is run. 

Copy the data below to a file named "Gene_RD_rpt.txt" and save in the same directory as your script.

GENE,READ_DEPTH
MLH1,230
PMS2,40
ABL1,50
PTEN,30
MLH1,230
PMS2,40
PMS2,40
ABL1,50
PTEN,30
PTEN,30
PTEN,30

'''

file_name = "GitHub/S-BG-S2-Mathew/genes.txt"

def remove_dup():
    with open(file_name, "r") as file:
        lines = file.readlines()

    # Remove duplicates
    unique_lines = list(set(lines))

    # write out 
    with open(file_name, "w") as file:
        file.writelines(unique_lines)

remove_dup()

poo