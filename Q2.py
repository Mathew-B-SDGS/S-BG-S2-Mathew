
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
def calculate_mean_read_depth():
 with open ("genes.txt") as file:
    sum_read_depth=0
    num_genes=0
    for line in file:
        if line == "GENE,READ_DEPTH\n":
           pass
        else:
            gene, read_depth=line.strip().split(",")
            sum_read_depth+=int(read_depth)
            num_genes+=1

    mean_read_depth = sum_read_depth/num_genes
    return mean_read_depth
 
a=calculate_mean_read_depth()
print(a)