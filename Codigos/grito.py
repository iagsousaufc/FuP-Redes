casos = input()

for caso in range(casos):
	tam_grito = raw_input().split(" ")
	s_op = raw_input().split(" ")

	tam = int(tam_grito[0])
	grito = int(tam_grito[1])

	op = []

	for i in s_op:
		op.append(int(i))

	for i in range(tam):
		if op[i] == grito:
			if i == 0:
				op[i+1] *= -1
			elif i == (tam-1):
				op[i-1] *= -1
			else:
				op[i-1] *= -1
				op[i+1] *= -1

	for i in op:
		print i,
	print ' '
