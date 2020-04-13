##Function for string to integer list
dt = open('data.txt', 'r').read()

def strtolist(x):
    counter = 0
    counter2 = 0
    temp_number = ''
    new_data = []
    safety = 0
    
    for i in x:
        if i is not ' ':
            temp_number = temp_number + i
            
    
        if i == ' ':
            new_data.append(int(temp_number))
            temp_number = ''
            

        if x[safety] == x[-1]:
            new_data.append(int(temp_number))
            temp_number = ''
            
        
        safety = safety + 1        
    
    return new_data

integer_list = strtolist(dt)

