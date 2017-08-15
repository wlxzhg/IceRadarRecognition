import random
def creatRadar(x,y):
	ret = []
	i = x;
	while i > 0:
		row = []
		j = y
		while j > 0:
			row.append(random.randint(-10000,10000))
			j = j - 1
		ret.append(row) 
		i = i - 1
	return ret
def recognitionRadarI(radar):
	ret = [0,0,0,0,0,0,0,0,0,0]
	sum = 0;
	for row in radar:
		for col in row:
			sum += col
	ret[sum % 10] = 1
	return ret
