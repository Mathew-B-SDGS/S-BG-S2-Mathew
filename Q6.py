### Question 6 ### 
'''
Given a DNA sequence produce the reverse compliment

example input sequence:

'ATGCGTCAGTAAAATTTACG'

'''

def reverse_compliment(input):
    key={
        "A":"T",
        "C":"G",
        "T":"A",
        "G":"C"
    }
    for base in input:
        compliment_base= key[base]
        reversed_strand=""
        reversed_strand+=compliment_base

print(reverse_compliment("ATGCGTCAGTAAAATTTACG"))
