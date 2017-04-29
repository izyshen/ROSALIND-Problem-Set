## takes in a FASTA format of DNA strands and places them in a dictionary

def condense(filename):
    dna = open(filename, 'r')
    dna_lines = dna.readlines()
    dic = {}
    for line in dna_lines:
        if '>' in line:
            line = line.replace('>', '')
            line = line.replace('\n', '')
            seq = ''
            dic[line] = seq
            curr = line
        else:
            if '\n' in line:
                line = line.replace('\n', '')
            dic[curr] += line
    dna.close()
    return dic


## prints the name and percentage of the DNA strand with the highest GC content

def highest_GC_content(filename):
    dictionary = condense(filename)
    ID = ''
    highest_percent = 0
    for DNA_str in dictionary:
        percent = (dictionary[DNA_str].count('G') + \
                   dictionary[DNA_str].count('C')) / \
                   len(dictionary[DNA_str])
        if highest_percent < percent:
            ID = DNA_str
            highest_percent = percent
    print(ID)
    print(highest_percent*100)
    return
