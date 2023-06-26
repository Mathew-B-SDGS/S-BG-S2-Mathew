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

file_name = "Gene_RD_rpt.txt"

def remove_dup(file_name, new_file_name):
    '''
    function takes and 2 inputs: the target file path, and the output file name
    returns the values into a new file 
    '''
    with open(file_name, "r") as file:
        lines = file.readlines()

    unique_lines = []
    unique_lines.append(lines[0])  # Add the header line as the first line in the unique lines list

    # Iterate through each line starting from the second line
    for line in lines[1:]:
        if line not in unique_lines:  # Check if the line is not already present in the unique lines list
            unique_lines.append(line)  # Add the line to the unique lines list

    # Open the file in write mode to overwrite the content
    with open(new_file_name, "w") as file:
        file.writelines(unique_lines)  # Write the unique lines to the file

remove_dup(file_name)

