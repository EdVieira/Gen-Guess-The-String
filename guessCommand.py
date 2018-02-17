#encoding: utf-8

#:
#Lorem ipsum dolor sit amet, vel morbi consecteteur.

#:
#Lorem ipsum dolor sit amet, tristique cras, wisi ante mollis nulla molestie eros, sed felis vestibulum, mauris sed tincidunt lectus vestibulum duis. Nulla ultricies amet erat accumsan eget, leo magna felis rutrum suscipit ut eget. Ante luctus posuere dolor in pede ut.

#:
#Lorem ipsum dolor sit amet, tristique cras, wisi ante mollis nulla molestie eros, sed felis vestibulum, mauris sed tincidunt lectus vestibulum duis. Nulla ultricies amet erat accumsan eget, leo magna felis rutrum suscipit ut eget. Ante luctus posuere dolor in pede ut. Sapien eleifend ultricies hac a ipsum mauris, est ac dolor. Lacinia mauris sed id ut phasellus diam, nulla consectetuer in curabitur enim parturient ligula, vitae vel laoreet aliquam egestas enim.


import random, sys

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

def rank(goal, a):
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
		if rank(goal, population[i]) >= rank(goal, better1):
			better1 = population[i]
	for i in range(len(population)):
		if rank(goal, population[i]) >= rank(goal, better2) and population[i] != better1:
			better2 = population[i]
	parents = [better1, better2]
	return parents


##Get comand line second to antepenult argument after self
word = ' '.join(sys.argv[1:-1])
##Get comand line last argument
amount = int(''.join(sys.argv[-1:]))
##generate first population (random individuals)
childs = randPopulate(word, amount)

##select two higher ranked as parents
parents = selection(childs, word)

##iterations counter to meassure results
iterations = 0
z = "batata"
print len(z)
##heuristc function loop
while parents[0] != word or parents[1] != word:

	##generate a new population from parents (past population higher ranks)
	childs = populate(parents[0], parents[1], amount)

	##select two higher ranked as parents
	parents = selection(childs, word)

	##choose and show on screen the most ranked parent
	if rank(word, parents[0]) > rank(word, parents[1]):
		print parents[0],"\n"
	else:
		print parents[1],"\n"

	##increment iteration counter
	iterations = iterations + 1

	##loop stop clause is when we find the perfect solution as one of parents
	if word == parents[0]:
		parents = parents[0]
		break
	if word == parents[1]:
		parents = parents[1]
		break

##return results when finished approaching
print "Sentence given:\n", parents
print "Number of iterations: ", iterations
print "Word", len(parents)