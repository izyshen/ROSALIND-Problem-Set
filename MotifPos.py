## takes in a file where the first line has a string of DNA, s, and
## the second line has a motif, t, shorter than the s. It will then produce
## the positions at which t is found in s. 

def pos_of_motif(filename):
    file = open(filename, 'r')
    DNA = file.readline().replace('\n', '')
    motif = file.readline().replace('\n', '')
    file.close()
    pos = []
    for i in range(len(DNA)-len(motif)):
        if DNA[i:i+len(motif)] == motif:
            pos.append(i+1)
    return pos
