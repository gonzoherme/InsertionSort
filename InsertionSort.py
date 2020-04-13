from stringtolist import strtolist


dt = open('data.txt', 'r').read()
integer_list = strtolist(dt)
intlist = integer_list
print(intlist)

counter = 0
counter2 = 0
temp = 0


repetitions  = []
check = []
for i in intlist:
    if i in check:
        repetitions.append(i)

    check.append(i)

for i in repetitions:
    intlist.remove(i)

while counter <= len(intlist) -1:
    
    if intlist[counter] > intlist[counter - 1]:
        pass

    else:
        while True:
            
            if counter2 == counter:
                counter2 = 0
                break
            
            if intlist[counter2] < intlist[counter]:
                pass


            else:
                temp = intlist[counter]
                intlist.remove(intlist[counter])
                intlist.insert(counter2, temp)
                counter2 = 0
                break



            counter2 = counter2 +1

    counter = counter + 1

c = 0    
for i in repetitions:
    while c<= len(intlist) - 1:
        if intlist[c] == i:
            intlist.insert(c, i)
            c = 0
            break
        
        c = c+1

print(intlist)
