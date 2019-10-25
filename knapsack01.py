import random
vol=0
class Item(object):# a class for items with tow property of value and weight of item
    def __init__(self, v, w):
        self.value = v
        self.weight = w


def random_genotype(size): #create random genotype in range of initial population
    return [genotype() for x in range (0,size)]

def genotype():#create a random genotype stream of 1s and 0s
    return [random.randint(0,1) for x in range (0,len(ITEMS))]

def fitness(genotype): #evaluate fittness for a genotype with many to one mechanisem
    sum_value=0
    sum_weight=0
    itemNum=0
    for i in  range (len(genotype)):
        if(genotype[i]==1 and (sum_weight + ITEMS[itemNum].weight < vol) ):
            sum_value += ITEMS[itemNum].value
            sum_weight += ITEMS[itemNum].weight
        
        else:
            i=len(genotype)
        itemNum += 1
            
    return sum_value

def parent_pool(population):#create Parent pool for reproduction
    return [parent_pool_select(population) for _ in range(1000)]

def parent_pool_select(population):#randomly select to parent in population and select the best one for parents pool
    candidates= [random.choice(population) for _ in range(2)]
    fitcandids=[fitness(j) for j in candidates]
    return candidates[fitcandids.index(max(fitcandids))]


def mutate(child):# mutate childs
    r = random.randint(0,len(child)-1)
    if child[r] == 1:
        child[r] = 0
    else:
        child[r] = 1
    return child

def evolve(pool):# select 2 random parent from parent pool to reproduction and crossover
    children = []

    while len(children) < 500:
        male = pool[random.randint(0, len(pool) - 1)]
        female = pool[random.randint(0, len(pool) - 1)]

        s = len(male)
        c=random.randint(0, s - 1)
        if random.randint(0,100) < 70:
            child = male[:c] + female[c:]
            child2= female[:c] + male[c:]
            mutate(child)
            mutate(child2)
            children.append(child)
            children.append(child2)
        else:
            mutate(male)
            mutate(female)
            children.append(male)
            children.append(female)
    return children

if __name__ == "__main__":
    generation = 1
    n = int(input("Insert number of ITEMS: "))
    vol=9*n
    ITEMS = [Item(random.randint(5,3*n),random.randint(5,3*n)) for x in range (0,n)]
    population = random_genotype(500)
    
    x=1
    generation=1
    best=0
    max1=0
    while x:
        population= evolve(parent_pool(population))
        fit = [fitness(x) for x in population]
        best=max(fit)

        if  (generation % 25 == 0):
            if (best==max1):
                x=0
            else:
                max1=best

        generation +=1
        print ("Generation",generation,population[fit.index(max(fit))],"Profit==",max(fit) )
    print ('*************************************************************************************')
    print("solution==", population[fit.index(max(fit))],"Profit==",max(fit))
    print(" value=","         Weight=","       napsack vol=")
    for i in ITEMS:
     print ("     ",i.value,"          Weight=",i.weight,"      vol=",vol)
    print("************************************************************************************************")
    n = int(input("Press any key to Exit: "))
