
'''

Write a function that takes as input integers N and L to generate N million random DNA fragments of length L

'''
#N number of short reads, 
#L length of the short reads.
 
import random

def generator(L,N):
    BaseCoding={1:"A",2:"T",3:"C",4:"G"}
    Read=""
    Nillion=int(N)*100000
    with open("seq.fastq","w") as file:
        for number in range(Nillion):
            Read = "\n@ReadNumber" + str(number) + "\n"
            for length in range(L):
                BaseRandom=(random.randint(1,4))
                Read+=BaseCoding[BaseRandom]
            file.write(Read)


print(generator(50,5))




'''
make a range of N 
loop through the range 
make a header based on N 
for range of L 
random base 
'''