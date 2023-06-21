### Question 6 ### 
'''
Given a DNA sequence produce the reverse compliment

example input sequence:

'ATGCGTCAGTAAAATTTACG'

'''

def reverse_complement(input_seq):
    key = {
        "A": "T",
        "C": "G",
        "T": "A",
        "G": "C"
    }

    reversed_seq = ""
    for base in input_seq:
        complement_base = key[base]
        reversed_seq = complement_base + reversed_seq

    return reversed_seq

print(reverse_complement("ATGCGTCAGTAAAATTTACG"))
