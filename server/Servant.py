import xidianRadar

class RadarUtilI(xidianRadar.RadarUtil):
	def recognitionRadar(self,r,current=None):
		ret = [0,0,0,0,0,0,0,0,0,0]
		sum = 0;
		for row in r:
			for col in row:
				sum += col
		ret[sum % 10] = 1
		ret.append(sum)
		return ret