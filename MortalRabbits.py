## takes in a file of two integers, n months and m life span and produces
##    the number of rabbit pairs in month n

def mortal_rabbits(filename):
    situation = open(filename, 'r')
    data = situation.readline().split(' ')
    situation.close()
    months = int(data[0])
    lifespan = int(data[1])
    Fn2 = 1
    Fn1 = 1
    if months == 1 or months == 2:
        return 1
    prev_rabbits = [1, 1, 1]
    for m in range(months)[2:]:
        if len(prev_rabbits) <= lifespan:
            temp = Fn2
            Fn2 = Fn1
            Fn1 = temp + Fn1
            prev_rabbits.append(Fn1)
        else:
            rabbit_deaths = prev_rabbits[0]
            prev_rabbits = prev_rabbits[1:]
            temp = Fn2
            Fn2 = Fn1
            Fn1 = temp + Fn1 - rabbit_deaths
            prev_rabbits.append(Fn1)
    return prev_rabbits[-1]
