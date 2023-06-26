### Question 7 ### 
'''
Given a list of DNA sequences in align_sequences.txt write a script to determine the number of sequences that match the reference:

REF = 'GATCTAAAAAAAGCCCATACGGCGCGCA'

Copy the data below to a file named "align_sequences.txt" and save in the same directory as your script.

GATCTAAAAAAAGCCCATACGGCGCGCA
CCTCTAAAAAAAGCCGTTACGGCGCGCA
CCTCTAAAAAAAGCCGTTACGGCACGCA
GATCTAAAAAAAGCCCATACGGCGCGCA
GATCTAAAAAAAGCCCATACGGCGCGCA
CCTCTTTTAAAAGCCGTTACGGCACGCA
AATCTGGTAAAAGCCGTTACGGCACCCA
CCTCTTTTAAAAGCCGTTACGGCACGCA
AATCTGGTAAAAGCCGTTACGGCACCCA
CCTCTAAAAAAAGCCGTTACGGCACGCA
CCTCTTTTAAAAGCCGTTACGGCACGCA
AATCTGGTAAAAGCCGTTACGGCACCCA
CCTCTTTTAAAAGCCGTTACGGCACGCA
GATCTAAAAAAAGCCCATACGGCGCGCA
AATCTGGTAAAAGCCGTTACGGCACCCA
CCTCTAAAAAAAGCCGTTACGGCACGCA
GATCTAAAAAAAGCCCATACGGCGCGCA
GATCTAAAAAAAGCCCATACGGCGCGCA
GATCTAAAAAAAGCCCATACGGCGCGCA
GATCTAAAAAAAGCCCATACGGCGCGCA

'''



REF = "GATCTAAAAAAAGCCCATACGGCGCGCA"

def alignment(target):
    counter = 0
    with open("genes.txt", "r") as file:
        lines = file.readlines()#open files and add them to lines
        for line in lines:#loop in the lines
            #removes the new line character from the string as it prevents it matching. 
            line=line.rstrip("\n")
            #print(line)
            if line == target:#check to see if theres a match, even with escape character 
                counter += 1
    return counter

print(alignment(REF))




