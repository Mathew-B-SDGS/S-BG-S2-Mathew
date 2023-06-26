### Question 10 (Rosalind question) ### 

'''
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

Copy the data below to a file named "Rosalind_GC.txt" and save in the same directory as your script.

>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT

'''

def highest_gc():
    with open("seq1.txt", "r") as file:
        data = file.readlines()
        dict_gc = {}
        for i, lines in enumerate(data):
            if lines.startswith(">",):
                id = lines.strip(">Rosalind_\n")
                next_line = data[i + 1] 
                gc_count = next_line.count('G') + next_line.count('C')
                total_count = len(next_line)
                gc_content = (gc_count / total_count) * 100
                dict_gc.update({id: gc_content})
        max_gc = max(dict_gc, key=dict_gc.get)
        return max_gc, dict_gc[max_gc]


print(highest_gc())



