## file has format of 6 numbers on one line (1 2 0 0 0 1) where
## the position of each number represents the number of individuals
## possessing each genotype
## 1. AA-AA
## 2. AA-Aa
## 3. AA-aa
## 4. Aa-Aa
## 5. Aa-aa
## 6. aa-aa
## produces the expected number of offspring with the dominant phenotype.
## each mating produces two offspring. 


def expected_offspring(filename):
    data = open(filename, 'r')
    pop = data.readline().split(' ')
    dom_phen = [1, 1, 1, 0.75, 0.5, 0]
    expected = 0
    for i in range(len(pop)):
        expected += (dom_phen[i]*int(pop[i]))*2
    return int(expected)
