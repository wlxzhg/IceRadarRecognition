import sys,Ice
import xidianRadar
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

with Ice.initialize(sys.argv) as communicator:
	base = communicator.stringToProxy("RadarUtil:default -p 10000")
	radarUtil = xidianRadar.RadarUtilPrx.checkedCast(base)
	if not radarUtil:
		raise RuntimeError("Invalid proxy")
	r = creatRadar(2,2)
	print(r)
	ret = radarUtil.recognitionRadar(r)
	print(ret)