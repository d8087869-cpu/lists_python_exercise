agents = ['alpha' , 'bravo' , 'charlie' , 'delta' , 'echo']
print(agents)
print (agents[::4])
print(agents[2])
#4
print(agents[1:4])
#5
agents.append('foxtrot')
print(agents)
#6
agents.insert (2 , 'zulu')
print(agents)
#7 
agents[1]=7
print(agents)
#8
print(len(agents))