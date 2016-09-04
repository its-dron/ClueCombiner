clue_file = "clues.txt"
targets = [98, 122, 67, 115, 140, 109, 46, 53, 117, 136, 31, 87, 106, 132, 74]
targets.sort()

numbers = []
clues = []

with open(clue_file) as f:
    for line in f:
        number, clue = line.split("\t")
        numbers.append(int(number))
        clues.append(clue[:-1])
    
r = {t: [] for t in targets}

N = len(numbers)
for i in range(N):
    n1 = numbers[i]
    for j in range(i,N):
        n2 = numbers[j]
        s = n1+n2
        if s in r:
            r[s].append( (str(n1) + ", " + str(n2), clues[i] + ", " + clues[j]) )
            
for key in targets:
	if len(r[key]) > 0:
		print key
		for match in r[key]:
			print " - " + match[0], match[1]
