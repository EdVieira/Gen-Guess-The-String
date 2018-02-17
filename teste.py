#encoding: utf-8
#(3SEG):Lorem ipsum dolor sit amet, vel morbi consecteteur.

#(5MIN):Lorem ipsum dolor sit amet, tristique cras, wisi ante mollis nulla molestie eros, sed felis vestibulum, mauris sed tincidunt lectus vestibulum duis. Nulla ultricies amet erat accumsan eget, leo magna felis rutrum suscipit ut eget. Ante luctus posuere dolor in pede ut.

#Lorem ipsum dolor sit amet, tristique cras, wisi ante mollis nulla molestie eros, sed felis vestibulum, mauris sed tincidunt lectus vestibulum duis. Nulla ultricies amet erat accumsan eget, leo magna felis rutrum suscipit ut eget. Ante luctus posuere dolor in pede ut. Sapien eleifend ultricies hac a ipsum mauris, est ac dolor. Lacinia mauris sed id ut phasellus diam, nulla consectetuer in curabitur enim parturient ligula, vitae vel laoreet aliquam egestas enim.


import random, sys

def randGen(entrada):
	return random.random()

def cruzamento(a, b):
	quebra = int(random.randint(0, len(a)))
	parte1 = a[:quebra]
	parte2 = b[quebra:]
	return parte1 + parte2

def mutacao(meta, a):
	contador1 = 0
	for i in range(len(meta)):
		if meta[i] != a[i]:
			break
		else:
			contador1 = contador1 + 1
	contador2 = 0
	for i in range(len(meta)-1, 0, -1):
		if meta[i] != a[i]:
			break
		else:
			contador2 = contador2 + 1
	
	indice = random.randint(contador1,len(a) - 1 - contador2)
	altura = random.randint(0,10)
	a = a[:indice] + chr(random.randint(32, 126)) + a[1 + indice:]
	return a

def populacao(pai1, pai2, n):
	filho = [""]
	for i in range(n-1):
		filho.append("")

	for i in range(len(filho)):
		filho[i] = cruzamento(pai1, pai2)	

	for i in range(len(filho)):
		filho[i] = mutacao(palavra, filho[i])
	return filho

def fitness(meta, a):

	fator = 0

	for i in range(len(meta)):

		if meta[i] == a[i]:
			fator = fator + 1
		else:
			fator = fator - 1

	if len(a) > len(meta):
		fator = fator - len(a)
	return int(fator)
	

#def selecao(populacao, meta, controle, contagem):
#	melhor = ""
#	for i in range(len(populacao)):
#		if fitness(palavra, filho[0]) <= fitness(palavra, filho[1]):
#			if len(filho[0]) <= len(filho[1]):
#				pai[0] = filho[0]
#			else:
#				pai[0] = filho[1]
#	
####
#	primeiro = controle
#	melhor = "~"*len(meta)
#	for i in range(len(populacao)):
#		fitMelhor = fitness(meta, melhor)
#		individuo = populacao[i]
#		fitIndividuo = fitness(meta, individuo)
#		if fitIndividuo < fitMelhor or individuo != controle:
#			melhor = populacao
#	if contagem > 0:
#		pais = [primeiro, melhor]
#		return pais
#	return selecao(populacao, meta, melhor, contagem+1)


####

print 'Write a sentence:'
palavra = raw_input()
qtd = 100


pai = ["", ""]

pai[0] = randGen(palavra)
pai[1] = randGen(palavra)

while pai[0] != palavra or pai[1] != palavra:
	filho = populacao(pai[0], pai[1], qtd)


##preciso fazer uma função para seleção natural e flexibilizar mais o código...
	if fitness(palavra, filho[0]) >= fitness(palavra, filho[1]):
		if len(filho[0]) <= len(filho[1]):
			pai[0] = filho[0]
		else:
			pai[0] = filho[1]
	else:
		if len(filho[1]) <= len(filho[0]):
			pai[0] = filho[1]
		else:
			pai[0] = filho[0]

	if fitness(palavra, filho[2]) >= fitness(palavra, filho[3]):
		if len(filho[2]) <= len(filho[3]):
			pai[1] = filho[2]
		else:
			pai[1] = filho[3]
	else:
		if len(filho[3]) <= len(filho[2]):
			pai[1] = filho[3]
		else:
			pai[1] = filho[2]
	print pai
	if palavra == pai[0]:
		pai = pai[0]
		break
	
	if palavra == pai[1]:
		pai = pai[1]
		break
print "Sentence given:"
print pai
