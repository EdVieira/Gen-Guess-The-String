#encoding: utf-8

#:
#Lorem ipsum dolor sit amet, vel morbi consecteteur.

#:
#Lorem ipsum dolor sit amet, tristique cras, wisi ante mollis nulla molestie eros, sed felis vestibulum, mauris sed tincidunt lectus vestibulum duis. Nulla ultricies amet erat accumsan eget, leo magna felis rutrum suscipit ut eget. Ante luctus posuere dolor in pede ut.

#:
#Lorem ipsum dolor sit amet, tristique cras, wisi ante mollis nulla molestie eros, sed felis vestibulum, mauris sed tincidunt lectus vestibulum duis. Nulla ultricies amet erat accumsan eget, leo magna felis rutrum suscipit ut eget. Ante luctus posuere dolor in pede ut. Sapien eleifend ultricies hac a ipsum mauris, est ac dolor. Lacinia mauris sed id ut phasellus diam, nulla consectetuer in curabitur enim parturient ligula, vitae vel laoreet aliquam egestas enim.


import random

def randGen(goal):
	lenGoal = len(goal)
	gen = ""
	for i in range(lenGoal):
		gen = gen + chr(random.randint(0, 255))
	return gen

def crossover(a, b):
	broke = int(random.randint(0, len(a)))
	part1 = a[:broke]
	part2 = b[broke:]
	return part1 + part2

def mutation(a):
	index = random.randint(0,len(a))
	a = a[:index] + chr(random.randint(32, 126)) + a[1 + index:]
	return a

def randPopulate(goal, n):
	childs = [""]
	for i in range(n-1):
		childs.append("")
	for i in range(len(childs)):
		childs[i] = randGen(word)
	return childs

def populate(parent1, parent2, n):
	childs = [""]
	for i in range(n-1):
		childs.append("")
	for i in range(len(childs)):
		childs[i] = crossover(parent1, parent2)	
	for i in range(len(childs)):
		childs[i] = mutation(childs[i])
	return childs

def fitness(goal, a):
	factor = 0
	previous = False
	for i in range(len(goal)):
		if goal[i] == a[i]:
			if previous:
				factor = factor + 3
				previous = True
			else:
				factor = factor +1
				previous = True
		else:
			if not previous:
				factor = factor - 3
				previous = False
			else:
				factor = factor - 1
				previous = False
	if len(a) > len(goal):
		factor = factor - len(a)
	return int(factor)
	

def selection(population, goal):
	better1 = population[0]
	better2 = population[0]
	for i in range(len(population)):
		if fitness(goal, population[i]) >= fitness(goal, better1):
			better1 = population[i]
	for i in range(len(population)):
		if fitness(goal, population[i]) >= fitness(goal, better2) and population[i] != better1:
			better2 = population[i]
	parents = [better1, better2]
	return parents


print 'Write a sentence:'
word = raw_input()
print "Lenght: ",len(word)
amount = input("Population size: ")

childs = randPopulate(word, amount)
parents = selection(childs, word)

iterations = 0

while parents[0] != word or parents[1] != word:
	childs = populate(parents[0], parents[1], amount)
	parents = selection(childs, word)
	if fitness(word, parents[0]) > fitness(word, parents[1]):
		print parents[0],"\n"
	else:
		print parents[1],"\n"
	iterations = iterations + 1
	#Stop clause
	if word == parents[0]:
		parents = parents[0]
		break
	
	if word == parents[1]:
		parents = parents[1]
		break

print "Sentence given:\n", parents
print "Number of iterations: ", iterations
