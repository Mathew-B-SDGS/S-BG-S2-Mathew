#answers to Problem 1 of the assignment 
# Name: Mathew B

#1.1

'''
Given a list of genes, e.g. 'MLH1 AHR BRCA2 BRCA1 MLH1 CAT'

    a. Write a function to return an list with the duplicates removed

    b. Write a function to return an list listing all the duplicate entries of the input list
'''


#opens the file using a with loop to close correctly after finishing
with open("genes.txt", "r") as file:
    #reads the file and splits it, removing any spaces
    genes_list = file.read().split()


#function to solve prob A.
def remove_duplicates(gene_list):
#changes the list into a Set to easily remove the duplicates as Sets dont allow duplicate values.
    genes_set = set(gene_list)
    return genes_set

#function to solve prob B.
def list_duplicates(gene_list):
    #creates 2 empty Dicts
    duplicates=[]
    singles=[]
    #for loop that iterates over the list adding duplicate values to a new variable, checking to see if the variable is already in the list 
    for genes in gene_list:
        if genes in singles:
            duplicates.append(genes)
        else:
            singles.append(genes) 
    return duplicates

a=remove_duplicates(genes_list)
b= list_duplicates(genes_list)
#print statement that returns the 2 values, appending them into a sentence. 
print("for problem A, the values are",", ".join(a), "\n for Problem B the answers are",", ".join(b))






