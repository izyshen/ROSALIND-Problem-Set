## takes in a file with a string of 'ACTG'

def count_nucleotides(filename):
    dna = open(filename, 'r')
    string = dna.readline()
    for i in 'ACGT':
        print(string.count(i))
    dna.close()
    return
