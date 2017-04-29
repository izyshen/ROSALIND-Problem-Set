## Takes in a file with a collection of DNA strings in FASTA format 
## and produces a directed graph where the last three nucleotides of one sequence
## match up with the first three nucleotides of another sequence.
## sequence one and two cannot be the same. 

def adjacency_list(filename):
    data = open(filename, 'r')
    d = {}
    for line in data.readlines():
        line = line.replace('\n', '')
        if '>' in line:
            line = line.replace('>', '')
            d[line] = ''
            curr_line = line
        else:
            d[curr_line] += line
    data.close()
    m = d.keys()
    for nt1 in m:
        for nt2 in m:
            curr = [nt1]
            if d[nt1][-3:] == d[nt2][0:3] and d[nt1] != d[nt2]:
                print(nt1 + ' ' + nt2)
    return
