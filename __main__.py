from rich import print
from .barchart import SimpleBarChart
from random import randint
import math

sbc = SimpleBarChart("simple bar chart demo #1")

# sbc.plot([0, 1, 2, 3, 4, 5, 6], separator="|", separator_style="#BADA55")

# print(str(sbc))

def lerp(a, b, t):
	return a+(b-a)*t

data_a = [randint(95, 100) for i in range(50)]
data_b = [randint(95, 100) for i in range(50)]

import os
import time
for i in range(200):
	# os.system("clear")
	sbc.plot([lerp(a, b, math.sin(i/20)*.5+.5) for a, b in zip(data_a, data_b)], separator="#", separator_style="#111111")
	print(str(sbc))
	time.sleep(0.1)