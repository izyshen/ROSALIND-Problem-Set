def common_substring(filename):
    data = open(filename, 'r')
    d = data.readlines()

    ## produces a list of DNA strands
    nuc = []
    for line in d:
        line = line.replace('\n', '')
        if '>' not in line:
            nuc.append(line)
    print(nuc)

    ## produces the common substrings in the first two strands of nuc
    longest = []
    for i in range(len(nuc[0])):
        m = i
        curr = ''
        for j in range(len(nuc[1])):
            if i < len(nuc[0]) and nuc[0][i] == nuc[1][j]:
                curr+=nuc[1][j]
                i+=1
            else:
                if curr != '':
                    longest.append(curr)
                curr = ''
                i = m
    print(longest)

    ## produces the common substrings of largest length
    l = len(longest[0])
    long = []
    for substring in longest:
        if len(substring) >= l:
            l = len(substring)
            long.append(substring)
    return long


####################################################


def common_substring2(filename):
    data = open(filename, 'r')
    d = data.readlines()

    ## produces a list of DNA strands
    nuc = []
    for line in d:
        line = line.replace('\n', '')
        if '>' not in line:
            nuc.append(line)
    print(nuc)
    all_substrings = []
    for i in range(len(nuc[0])):
        for r in list(range(len(nuc[0])))[:0:-1]:
            if nuc[0][i:r+1] not in all_substrings:
                all_substrings.append(nuc[0][i:r+1])
    print(all_substrings)
    for other_nuc in nuc[1:]:
        for substring in all_substrings:
            if substring not in other_nuc:
                all_substrings.remove(substring)
    print(all_substrings)
    return
