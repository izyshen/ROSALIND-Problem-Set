## takes in a file and produces the complement strand of DNA

def rev_complement(filename):
    dna = open(filename, 'r')
    string = dna.readline()
    new_line = ''
    for i in string:
        if i == 'A':
            new_line += 'T'
        elif i == 'T':
            new_line += 'A'
        elif i == 'G':
            new_line += 'C'
        elif i == 'C':
            new_line += 'G'
    dna.close()
    return new_line[::-1]
