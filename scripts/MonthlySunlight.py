import math

for i in range(12):
	s = 143 * (math.cos(2 * i * math.pi / 12) + 1) + 215
	# print('%.2f' % s)

	correction = 0.38*(math.cos(2*i*math.pi/12 + 13*math.pi/12)+1)+0.25
	print(correction)