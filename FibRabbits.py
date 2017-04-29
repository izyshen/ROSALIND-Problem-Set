## reads a file of two integers on one line: n months and k rabbits produced
##    during each round of reproduction

def fib_rabbits(filename):
    situation = open(filename, 'r')
    mon_reproduction = situation.readline().replace('\n', '').split(' ')
    situation.close()
    Fn_1 = 1
    Fn = 1
    if int(mon_reproduction[0]) <= 2:
        return 1
    else:
        for i in range(int(mon_reproduction[0]))[2:]:
            temp = Fn_1 * int(mon_reproduction[1])
            Fn_1 = Fn
            Fn = temp+Fn_1
        return Fn
