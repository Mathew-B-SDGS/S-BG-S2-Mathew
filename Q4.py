
'''

Write a function that takes as input integers N and L to generate N million random DNA fragments of length L

'''
import random


def generator(length, number):
    '''
    function that takes input variable of #number for the amount of total reads and 
    #length of the amount of bases per reads. amplifies the inputted number value by a million. 
    writes out to a fasta file, in the correct format. 
    '''
    base_coding = "ATCG"  #  DNA bases in a string to be easily accessed. 
    read = ""  # Variable to store  read
    n_million = int(number) * 100000  # Total number of reads to generate times a million 
    
    with open("seq.txt", "w") as file:  # Open/creates a file for writing. 
        for number in range(n_million):  # Generate reads based on the total number
            read = "\n>ReadNumber" + str(number) + "\n"  # creates a Unique Identifier for each short read in fasta format, with a line break added. 
            for length_read in range(length):  
                base_random = random.randint(0, 3)  # Generate a random index for the base using the random module. numbers 0,1,2,3 are randomly chosen. 
                read += base_coding[base_random]  # this randomly chosen value is then used to index the string 'ATCG' adding a random base to the sequence.  
            file.write(read)  # Write the read to the file

# Example usage
generator(100, 10)  # Generate 10*1,000,000 short reads of length 100bp


