import copy
import random
# Consider using the modules imported above.

class Hat:
    
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        self.contents = []
        
        
        for key,value in self.kwargs.items():
            for i in range(value):
                self.contents.append(key)
               
    
    def draw(self, num_balls):
        
        self.content_copy = self.contents.copy() 
        
        if num_balls > len(self.contents):
            return(self.contents)
        
        else:
            draws = []
            
            
            for x in range(num_balls):
                #draws.append(random.choice(self.contents))
                draws.append(self.contents.pop(random.randrange(len(self.contents))))
           
            return(draws)
        
        
      

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    #track the number of times an experiment resulted in having all the expected balls drawn
    count = 0
    
    
    
    for _ in range(0,num_experiments):
        
        #set up empty dictionary to track balls that are drawn
        drawn = {}
        
        placeholder = copy.deepcopy(expected_balls)
        
        hat_copy = copy.deepcopy(hat)
 
        draw = hat_copy.draw(num_balls_drawn)
        #iterate through the drawn balls list and store the number of times drawn in drawn dictionary
        
        for y in draw:
            if y in drawn:
                drawn[y] += 1
            else:
                drawn[y] = 1
        
        #iterate through the keys of drawn, check if the value in drawn is equal to or greater than the amount in placeholder
        for i in list(placeholder.keys()):
        
            if i in drawn:
                if drawn[i] >= placeholder[i]:
                    placeholder[i] = 'Yes'
                else:
                    placeholder[i] = 'No'
                    
            else:
                continue
        
        if set(list(placeholder.values())) == {'Yes'}:
            count += 1
          
        else:
            continue
            
    return(count/num_experiments)
