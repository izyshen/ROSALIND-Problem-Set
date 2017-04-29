## takes in a file with two DNA strands on one line each
## and produces the number of point mutations

def point_mutations(filename):
    dna = open(filename, 'r')
    line_1 = dna.readline()
    line_2 = dna.readline()
    count = 0
    for i in range(len(line_1)):
        if line_1[i] != line_2[i]:
            count += 1
    dna.close()
    return count
