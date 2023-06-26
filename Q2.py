
### Question 2 ###
'''

A file (Gene_RD.txt) contains 2 columns of comma separated data with read depth values per gene. Write a function to extract the data and return the mean read depth across all genes.

Copy the data below to a file named "Gene_RD.txt" and save in the same directory as your script.

GENE,READ_DEPTH
MLH1,230
PMS2,40
ABL1,50
PTEN,30

 
'''

import csv
import statistics

def calculate_mean_read_depth():
 '''
 function that opens a file,  skips any header line. then splits each line into 2 variables, gene and read depth, striping the CSV. 
 checks that the read depth is an int before adding the to a sum value divided by the total genes. 
 returns the average read depth in the file. 
 '''
 with open ("genes.txt") as file:
    sum_read_depth=0
    num_genes=0
    for line in file:
        if line == "GENE,READ_DEPTH\n":
           pass
        else:
            #CSV within file, strip and split returns values from string using the , as a separator.
            gene, read_depth=line.strip().split(",")
            sum_read_depth+=int(read_depth)
            num_genes+=1

    mean_read_depth = sum_read_depth/num_genes
    return mean_read_depth
 


def calculate_mean_read_depth_v2():
 '''
 this function makes use oft he csv and statistics module to perform the above calculation in a more succinct manner. 
 the csv function allows the parsing of a file simply, with the statistics module easily returning the mean value from the table created by csv. 
 '''
 with open ("genes.txt") as file:
    reader = csv.DictReader(file)
    #places the data into a variable
    rows = [row for row in reader]
    #calls the function the mean value from statistics on all values in the data structure, ensuring value is an int. 
    return statistics.mean([int(row['READ_DEPTH']) for row in rows])
 

print(calculate_mean_read_depth(), calculate_mean_read_depth_v2())