## takes in a file and produces a string of DNA -> RNA

def change_to_rna(filename):
    dna = open(filename, 'r')
    string = dna.readline()
    new_line = ''
    for i in string:
        if i == 'T':
            new_line += 'U'
        else:
            new_line += i
    dna.close()
    return new_line
