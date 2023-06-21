
'''

Write a function that takes as input integers N and L to generate N million random DNA fragments of length L

'''
import random
#N number of short reads, 
#L length of the short reads.
def generator(length,number):
    #Dict assigning a value key for each Base
    base_coding="ATCG"
    read=""
    #Multiplying the N input value to a factor of a million 
    n_million=int(number)*100000
    #Opening a Fastq file to keep data
    with open("seq.fastq","w") as file:
        #loop through the set range
        for number in range(n_million):
            #formatted as a Fastq File, with the @ number and read name 
            read = "\n>ReadNumber" + str(number) + "\n"
            #loop to determine the length of sequence. 
            for length_read in range(length):
                #randomly choose a number
                base_random=(random.randint(0,3))
                #use the random number to select a base from the dict
                read+=base_coding[base_random]
            #write out each variable 
            file.write(read)
# had issues with run time taking ages, as the read variable was getting to long, changed code to write the variable to the File after each loop.

print(generator(50,5))




'''
make a range of N 
loop through the range 
make a header based on N 
for range of L 
random base 
'''