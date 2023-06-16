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
    #changes the list into a set to easily remove the duplicates as sets dont allow dups.
    genes_set = set(genes_list)

# print(genes_set)
print("there are",len(genes_set),"unique genes in this set. which are listed as",(genes_set),)

duplicates=[]
singles=[]
for genes in genes_list:
    if genes in singles:
        duplicates.append(genes)
    else:
        singles.append(genes)
print(singles,duplicates)


