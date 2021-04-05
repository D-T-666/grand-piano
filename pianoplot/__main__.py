from rich import print
from .barchart import SimpleBarChart
from random import randint
import math

import os
import time

sbc_a = SimpleBarChart("simple bar chart demo #1")

lerp = lambda a, b, t: a+(b-a)*t

data_a = [randint(0, 100) for i in range(50)]
data_b = [randint(0, 100) for i in range(50)]

for i in range(20):
	sbc_a.plot([lerp(a, b, math.sin(i/10)*.5+.5) for a, b in zip(data_a, data_b)], separator="#", separator_style="#111111")
	sbc_a.render()


sbc_b = SimpleBarChart("simple bar chart demo #2")

lerp = lambda a, b, t: a+(b-a)*t

data_a = [randint(0, 100) for i in range(10)]
data_b = [randint(0, 100) for i in range(10)]

for i in range(200):
	sbc_b.plot([lerp(a, b, math.sin(i/10)*.5+.5) for a, b in zip(data_a, data_b)], separator="#", separator_style="#111111")
	sbc_b.render()