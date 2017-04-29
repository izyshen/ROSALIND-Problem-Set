## produces a list of codon triplets

def mRNA(seq):
    pos = 0
    new_seq = []
    while pos <= len(seq) - 2:
        new_seq.append(seq[pos:pos+3])
        pos+= 3
    return new_seq


## produces the polypeptide strand from an mRNA sequence

def polypeptide_producer(mRNAseq):
    polypeptide = []
    for codon in mRNAseq:
        if codon == 'UUU' or codon == 'UUC':
            polypeptide.append("F")      
        elif codon == 'AUG':
            polypeptide.append("M")        
        elif codon == 'UUA' or \
             codon == 'UUG' or \
             codon == 'CUU' or \
             codon == 'CUC' or \
             codon == 'CUA' or \
             codon == 'CUG':
            polypeptide.append("L")  
        elif codon == 'AUU' or \
             codon == 'AUC' or \
             codon == 'AUA':
            polypeptide.append ("I")
        elif codon == 'GUU' or \
             codon == 'GUC' or \
             codon == 'GUA' or \
             codon == 'GUG':
            polypeptide.append ("V") 
        elif codon == 'UCU' or \
             codon == 'UCC' or \
             codon == 'UCA' or \
             codon == 'UCG' or \
             codon == 'AGU' or \
             codon == 'AGC':
            polypeptide.append ("S")
        elif codon == 'CCU' or \
             codon == 'CCC' or \
             codon == 'CCA' or \
             codon == 'CCG':
            polypeptide.append ("P")
        elif codon == 'ACU' or \
             codon == 'ACC' or \
             codon == 'ACA' or \
             codon == 'ACG':
            polypeptide.append ("T")
        elif codon == 'GCU' or \
             codon == 'GCC' or \
             codon == 'GCA' or \
             codon == 'GCG':
            polypeptide.append ("A")
        elif codon == 'UAU' or \
             codon == 'UAC':
            polypeptide.append ("Y")
        elif codon == 'CAU' or \
             codon == 'CAC':
            polypeptide.append ("H")
        elif codon == 'CAA' or \
             codon == 'CAG':
            polypeptide.append ("Q")
        elif codon == 'AAU' or \
             codon == 'AAC':
            polypeptide.append ("N")
        elif codon == 'AAA' or \
             codon == 'AAG':
            polypeptide.append ("K")
        elif codon == 'GAU' or \
             codon == 'GAC':
            polypeptide.append ("D")
        elif codon == 'GAA' or \
             codon == 'GAG':
            polypeptide.append ("E")
        elif codon == 'UGU' or \
             codon == 'UGC':
            polypeptide.append ("C")
        elif codon == 'UGG':
            polypeptide.append ("W")
        elif codon == 'CGU' or \
             codon == 'CGC' or \
             codon == 'CGA' or \
             codon == 'CGG' or \
             codon == 'AGA' or \
             codon == 'AGG':
            polypeptide.append ("R")
        elif codon == 'GGU' or \
             codon == 'GGC' or \
             codon == 'GGA' or \
             codon == 'GGG':
            polypeptide.append ("G")
        elif codon == 'UAG' or \
             codon == 'UAA' or \
             codon == 'UGA':
            return polypeptide

## takes in a file of an mRNA strand and produces its polypeptide translation

def string_protein(filename):
    RNA = open(filename, 'r')
    mRNAseq = RNA.readline()
    helper = mRNA(mRNAseq)
    polypep = polypeptide_producer(helper)
    seq = ''
    for letter in polypep:
        seq += letter
    return seq
