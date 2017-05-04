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
