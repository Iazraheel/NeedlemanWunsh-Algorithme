#!/usr/bin/env python3

##Algorithme de NEEDLEMAN_WUNSH
import copy

class sequence:
	sequence=""
	def __init__(self,sequence):
		self.sequence=sequence

#Définition des couts
def score(matrice, i, j):
		left=matrice[i][j-1]
		right=matrice[i-1][j]
		diagonal=matrice[i-1][j-1]
		return max(left, right, diagonal)

class matrice:
	def __init__(self,x,y):
		self.x=x.sequence
		self.y=y.sequence
		self.m=len(x.sequence)
		self.n=len(y.sequence)
		self.matrice=[]
		self.firstFillOut()
		self.scoreFillOut()
		self.alignement=[]
		self.optimalAlignment()

	def toStreamAttribut(self):
		print(self.x, self.y, self.n, self.m)
	
	def score(x,y):
		if x==y:
			return 1
		else:
			return -1
	def firstFillOut(self):
		firstrow=[]
		for i in range(0,self.n+1):
			firstrow.append(0)
		self.matrice.append(firstrow)
		for i in range(0, self.m, 1):
			column=[]
			column.append(0)
			for j in range(0, self.n, 1):
				if j==0:
					column.append(0)
				else:
					column.append(0)
			self.matrice.append(column)
	
	#Methode d'affichage de la matrice		
	def toStreamMatrice(self):
		m_copy=self.matrice
		len_i=max(self.m, self.n)
		len_j=min(self.m, self.n)
		for i in range(0, len_j, 1):
			print("\n")
			for j in range(0,len_i, 1):
				print(self.matrice[j][i], end='')

	def scoreFillOut(self):
		
		for i in range(1, len(self.x), 1):
			for j in range(1, len(self.y),1):
				if self.x[i-1]==self.y[j-1]:
					w=1
				else:
					w=0
			
				m=self.matrice
				m[i][j]=score(m,i,j)+w
			
	def optimalAlignment(self):
		i=self.m
		j=self.n
		alignement1=[]
		#alignement1.append(self.x[i])
		#alignement2.append(self.y[j])
		alignement2=[]
		while i != 0 and j != 0:
			m=self.matrice
			diag=m[i-1][j-1]
			right=m[i-1][j]
			left=m[i][j-1]
			highter=max(diag, right, left)
			if highter==diag:
				alignement1.insert(0,self.x[i-1])
				alignement2.insert(0,self.y[j-1])
				i=i-1
				j=j-1
				continue

			if highter==right:
				alignement2.insert(0,self.x[i-1])
				alignement1.insert(0,"-")
				i=i-1
				j=j
				continue

			else:
				alignement1.insert(0,self.y[j-1])
				alignement2.insert(0,"-" )
				i=i
				j=j-1
		self.alignement.append(alignement1)
		self.alignement.append(alignement2)
		
		
seq1=sequence("GAATTCAGTTA")
seq2=sequence("GGATCGA")
m=matrice(seq1, seq2)
m.toStreamMatrice()
print("\n")
print(m.x, m.y)
print(m.alignement[0])
print(m.alignement[1])
