'''
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
scores=[42, 17, 95, 8, 61]
print(max(scores))
print(min(scores))
#10 

new_agents=agents.copy()
new_agents[0]='dave'
print(new_agents)
print(agents)
'''

#part2 

numbers =[3, 1, 4, 1, 5, 9, 2, 6]
print(sorted(numbers))
print(numbers)
numbers.sort ()
print(numbers)

#2
a =[1, 2, 3]
b =[4, 5, 6]
a+b 
print(a+b)
a,b.extend
print(a.extend(b))
#3
items = ['x', 'y', 'z', 'x', 'y', 'x']
print(items.count('x'))
del items[0]
del items[2]
del items[-1]
print(items)
#4 
data = [1, 2, 3, 4, 5]