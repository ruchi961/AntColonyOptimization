from random import randrange
vertices = ['A','B','C','D']
graph = {'A':['B','C','D'],'B':['A','C','D'],'C':['A','B','D'],'D':['A','B','C']}

weights = {'AB':10,'AC':10,'AD':30,'BC':40,'CD':20,'BD':10}
Pheromone={}
#decay rate
p=0.1

def initializePheromone():
    #initialize initial pheronome trails randomly
    #here a range of 1 - 50 is used for weights
    #random.random() can also be used, for no range of weights
    global Pheromone
    for key,value in graph.items():
        for i in value:
            if key+i not in Pheromone.keys() and i+key not in Pheromone.keys():
                Pheromone[key+i] = randrange(1,51)
    
    

def AOC(Pheromone):
    
    global weights,graph
    #5 ants
    initialVerticesCovered = []
    paths=[]
    for i in range(4):
        print("".center(80,"*"))
        
        discovered = []
        
        flag = True
        while flag:
            initial = randrange(0,4)
            if initial not in initialVerticesCovered:
                flag=False
        initialVerticesCovered.append(initial)

        initial = vertices[initial]
        j=0
        start = initial
        discovered.append(initial)
        #print("start",start,'initial',initial)
        while True:
            probabilities=[]
            sumHT=0
            possVertices = graph[initial].copy()
            #print("possible vertices",possVertices,graph[initial],graph)
            for i in possVertices:
                if initial+i in weights.keys():
                    H = round(1/weights[initial+i],3)                     
                elif i+initial in weights.keys():
                    H = round(1/weights[i+initial],3) 
              
                if initial+i in Pheromone.keys():
                    T = Pheromone[initial+i]                     
                elif i+initial in Pheromone.keys():
                    T = Pheromone[i+initial]
                    
                sumHT = sumHT + round((H*T),3)

            for i in possVertices:
                if initial+i in weights.keys():
                    H = round(1/weights[initial+i],3)                   
                elif i+initial in weights.keys():
                    H = round(1/weights[i+initial],3) 
              
                if initial+i in Pheromone.keys():
                    T = Pheromone[initial+i]                     
                elif i+initial in Pheromone.keys():
                    T = Pheromone[i+initial]
                    
                probabilities.append(round(((H*T)/sumHT),3))
            #print("probabilities",probabilities,"possVertices",possVertices)
            flag = True
            while flag:
                
                val = max(probabilities)
                
                val = probabilities.index(val)
                #print("val",val,"possVertices",possVertices,"probabilities",probabilities)
                nextVertex = possVertices[val]
                #print("nextVertex",nextVertex,"discovered",discovered)
                        
                if nextVertex not in discovered:
                    discovered.append(nextVertex)
                    #further path construction
                    initial = nextVertex
                    flag=False
                    
                else:
                    #print("hree",len(probabilities))
                    #go to initial vertex
                    probabilities.pop(val)
                    possVertices.pop(val)
                    if len(probabilities)==0:

                        discovered.append(start)
                        flag=False
                        #print("hree2",flag)

            #print("val",val,"possVertices",possVertices,"probabilities",probabilities,"discovered",discovered)
            if discovered[0] == discovered[-1] and len(discovered)!=1:
                print("discovered",discovered)
                paths.append(discovered)
                break
    #pheromone decay
    print("Before Decay: ",Pheromone)
    for key,value in Pheromone.items():
        Pheromone[key] = round(((1-p)*Pheromone[key]),3)
    print("After Decay: ",Pheromone)
    #print(paths)
    for key,value in Pheromone.items():
        sumVal=0
        for i in paths:
            string="".join(i)
            if key in string:
                #print("key",key,"string",string)
                sumVal = sumVal + round(( 1 / (len(string)-1) ),3)
##                l=0
##                print(weights)
##                for i in range(len(string)-1):
##                    if string[i]+string[i+1] in weights.keys():
##                        l = l + weights[string[i]+string[i+1]]
##                    elif string[i+1]+string[i] in weights.keys():
##                        l = l + weights[string[i+1]+string[i]]
##                sumVal = sumVal + l
        Pheromone[key] = Pheromone[key] + sumVal
    print("After adding Pheromone: ",Pheromone)
    return Pheromone
            
    
        
    

        
                
                        
        
                
            

        


initializePheromone()
print(Pheromone)
for i in range(10):
    Pheromone = AOC(Pheromone)
print(Pheromone)

path_best_score=[]
#printing the best path starting from the edge with maximum probability
for key,valuee in Pheromone.items():
    if valuee == max(list(Pheromone.values())):
        path_best_score.append(key[0])
        
start_pt=0
while (path_best_score[0]!=path_best_score[-1]) or len(path_best_score)==1:
    maxx_value=0
    for key,valuee in Pheromone.items():
        if key[0] == path_best_score[-1]:
            if valuee > maxx_value and (key[1] not in path_best_score[start_pt:]):
                print(1,key,valuee,path_best_score)
                maxx_value=valuee
                key_max = key[1]
        elif key[1] == path_best_score[-1]:
            if valuee > maxx_value and (key[0] not in path_best_score[start_pt:]):
                print(2,key,valuee,path_best_score)
                maxx_value=valuee
                key_max = key[0]
    #maxx_value==0 meaning the best path is the return to the starting point 
    if maxx_value==0:
        start_pt=1
        continue
                
    path_best_score.append(key_max)
print("The best path with Ant Colony Optimization is : ",path_best_score)    
path_best_score2=[]
path_best_score2.append(input("Enter the starting point: "))
start_pt=0
while (path_best_score2[0]!=path_best_score2[-1]) or len(path_best_score2)==1:
    maxx_value=0
    for key,valuee in Pheromone.items():
        if key[0] == path_best_score2[-1]:
            if valuee > maxx_value and (key[1] not in path_best_score2[start_pt:]):
                print(1,key,valuee,path_best_score2)
                maxx_value=valuee
                key_max = key[1]
        elif key[1] == path_best_score2[-1]:
            if valuee > maxx_value and (key[0] not in path_best_score2[start_pt:]):
                print(2,key,valuee,path_best_score2)
                maxx_value=valuee
                key_max = key[0]
    #maxx_value==0 meaning the best path is the return to the starting point 
    if maxx_value==0:
        start_pt=1
        continue
                
    path_best_score2.append(key_max)

print("The best path with Ant Colony Optimization is : ",path_best_score2)
