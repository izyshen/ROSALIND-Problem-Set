## consumes several DNA strands in a FASTA format file and produces 
## the consensus string and the profile matrix of the DNA strands

import re

def matrix(filename):
    data = condense(filename)
    DNA_strings = []
    for DNA in data:
        DNA_strings.append(data[DNA])
    dic = {'A': [0] * len(data[DNA]), 'C': [0] * len(data[DNA]), \
           'G': [0] * len(data[DNA]), 'T': [0] * len(data[DNA])}
    for strand in DNA_strings:
        for i in range(len(strand)):
            dic[strand[i]][i] += 1

    ## produces the consensus string
    consensus = ''
    for i in range(len(dic['A'])):
        most_common = ''
        count = 0
        for nucleotide in dic:
            if dic[nucleotide][i] > count:
                most_common = nucleotide
                count = dic[nucleotide][i]
        consensus += most_common
    print(consensus)
    
    ## produces the profile matrix    
    replace = {'[': '', ']': '', ',': '', '{': '', '}': '', "'": ""}
    profile = str(dic)
    replace = dict((re.escape(k), v) for k, v in replace.items())
    pattern = re.compile('|'.join(replace.keys()))
    profile = pattern.sub(lambda m: replace[re.escape(m.group(0))], profile)
    for char in 'ACTG':
        print(char + ': ' + ' '.join([str(count) for count in dic[char]]))
    return
