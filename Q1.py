#answers to Problem 1 of the assignment 
# Name: Mathew B

#1.1

'''

Given a list of genes, e.g. 'MLH1 AHR BRCA2 BRCA1 MLH1 CAT'

    a. Write a function to return an list with the duplicates removed

    b. Write a function to return an list listing all the duplicate entries of the input list


'''
# with open("genes.txt", "r") as list:
#     print(list)
#     GenesSet={}
#     for genes in list:
#         GenesSet=set((genes))
# print(GenesSet)
# print(len(GenesSet))

with open("genes.txt", "r") as file:
    genes_list = file.read().split()
    genes_set = set(genes_list)

# print(genes_set)
print("there are",len(genes_set),"unique genes in this set. which are listed as",(genes_set),)


