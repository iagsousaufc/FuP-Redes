s_lista = raw_input().split(" ")
lista = []
jedi = 0
sith = 0
for i in s_lista:
	lista.append(int(i))

meio = length(lista)/2

for i in range(0, meio):
	jedi += i

for i in range(meio, length(lista)):
	sith += i

if jedi == sith:
	print "empate"
elif jedi > sith:
	print "jedi"
else:
	print "sith"
