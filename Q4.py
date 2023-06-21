
'''

Write a function that takes as input integers N and L to generate N million random DNA fragments of length L

'''
import random

# N: number of short reads
# L: length of the short reads
def generator(length, number):
    base_coding = "ATCG"  #  DNA bases
    read = ""  # Variable to store  read
    n_million = int(number) * 100000  # Total number of reads to generate times a million 
    
    with open("seq.fastq", "w") as file:  # Open a file for writing, choose to format this into a FASTA. 
        for number in range(n_million):  # Generate reads based on the total number
            read = "\n>ReadNumber" + str(number) + "\n"  # Identifier for the read in fasta format
            for length_read in range(length):  # Generate the sequence of the read
                base_random = random.randint(0, 3)  # Generate a random index for the base using the random module. 
                read += base_coding[base_random]  # Add the randomly selected base to the read
            file.write(read)  # Write the read to the file

# Example usage
generator(100, 10)  # Generate 10*1,000,000 short reads of length 100bp


