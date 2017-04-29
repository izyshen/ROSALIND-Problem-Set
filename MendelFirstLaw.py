## reads a file of 3 positive integers on one line where the first number
## indicates the number of organisms that are homozygous dominant, heterozygous
## and homozygous recessive for a trait. It will then produce the probabilty
## of two random individual matings to produce an offspring with the dominant
## allele. 

def mendel_probability(filename):
    file = open(filename, 'r')
    hdom_het_hrec = file.readline().replace('\n', '').split(' ')
    file.close()
    for i in range(len(hdom_het_hrec)):
        hdom_het_hrec[i] = int(hdom_het_hrec[i])
    print(hdom_het_hrec)
    pop = sum(hdom_het_hrec)
    num_possibilities = pop*(pop-1)
    prob_hdom = hdom_het_hrec[0] / pop
    prob_het = hdom_het_hrec[1] / pop
    prob_hrec = hdom_het_hrec[2] / pop
    print(prob_hdom)
    print(prob_het)
    print(prob_hrec)
    prob_hdom_percent = prob_hdom
    prob_het_percent = ((hdom_het_hrec[0]/(pop-1))*prob_het) + \
                       ((((hdom_het_hrec[1]-1) / (pop-1))*prob_het) * 0.75) + \
                       (((hdom_het_hrec[2] / (pop-1))*prob_het) * 0.5)
    prob_hrec_percent = ((hdom_het_hrec[0] / (pop-1))*prob_hrec) + \
                        (((hdom_het_hrec[1] / (pop-1))*prob_hrec) * 0.5) + \
                        ((((hdom_het_hrec[2] - 1) / (pop-1))*prob_hrec) * 0)
    return prob_hdom_percent + prob_het_percent + prob_hrec_percent
