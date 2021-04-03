from rich import print
from .barchart import SimpleBarChart
from random import randint

sbc = SimpleBarChart("simple bar chart demo #1")
sbc.plot([randint(0, 100) for i in range(10)])

print(str(sbc))