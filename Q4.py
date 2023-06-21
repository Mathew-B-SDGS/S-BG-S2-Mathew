
'''

Write a function that takes as input integers N and L to generate N million random DNA fragments of length L

'''
import random
#N number of short reads, 
#L length of the short reads.
def generator(L,N):
    #Dict assigning a value key for each Base
    BaseCoding={1:"A",2:"T",3:"C",4:"G"}
    Read=""
    #Multiplying the N input value to a factor of a million 
    Nillion=int(N)*100000
    #Opening a Fastq file to keep data
    with open("seq.fastq","w") as file:
        #loop through the set range
        for number in range(Nillion):
            #formatted as a Fastq File, with the @ number and read name 
            Read = "\n@ReadNumber" + str(number) + "\n"
            #loop to determine the length of sequence. 
            for length in range(L):
                #randomly choose a number
                BaseRandom=(random.randint(1,4))
                #use the random number to select a base from the dict
                Read+=BaseCoding[BaseRandom]
            #write out each variable 
            file.write(Read)
# had issues with run time taking ages, as the read variable was getting to long, changed code to write the variable to the File after each loop.

print(generator(50,5))




'''
make a range of N 
loop through the range 
make a header based on N 
for range of L 
random base 
'''