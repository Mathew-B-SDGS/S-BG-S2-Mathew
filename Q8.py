# Question 7
def alignment(target):
    counter = 0
    with open("genes.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if line.strip() == target:
                counter += 1
    return counter

REF = 'GATCTAAAAAAAGCCCATACGGCGCGCA'
print(alignment(REF))

# Question 8
def alignment_score(target):
    score = 0
    with open("genes.txt", "r") as file:
        lines = file.readlines()
        num_lines = len(lines)
        for line in lines:
            for steps in range(len(line) - len(target) + 1):
                substring = line[steps : steps + len(target)]
                if substring == target:
                    score += steps
    percent_value = score / (len(target) * num_lines)
    return percent_value

REF = "GATCTAAAAAAAGCCCATACGGCGCGCA"
print(alignment_score(REF))
