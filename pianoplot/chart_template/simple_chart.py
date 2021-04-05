from ..terminal_size import get_terminal_size
from random import randint
from rich import print

class SimpleChart:
	def __init__(self, name="unnamed chart"):
		self.name = name
		self.w, self.h = get_terminal_size()
		self.margin = {
			't': 0,
			'r': 0,
			'b': 0,
			'l': 0
		}

		self.colors = [f'rgb({randint(64,255)},{randint(16,255)},{randint(64,255)})' for i in range(100)]

	def __str__(self):
		g = self.graph()
		gw= len(g[0][1])
		w = (self.w-2-self.margin['r']-self.margin['l'])
		s = ' '*((self.w-len(self.name))//2)+self.name+'\n'
		s += f"{' '*(self.margin['l']+(w-gw)//2)}┏{'━'*gw}┓\n"
		s += "\n".join([f"{' '*((w-gw)//4)}{label}{' '*((w-gw+2)//4)}┃{a}┃" for label, ra, a in g])+"\n"
		s += f"{' '*(self.margin['l']+(w-gw)//2)}┗{'━'*gw}┛	"
		return s

	def render(self):
		self.w, self.h = get_terminal_size()
		print(str(self))

	def plot(self, data, separator=" ", separator_style=""):
		self.data = data
		self.separator = separator
		self.separator_style = separator_style

	def graph(self):
		return " ", "[red]graph() function has not been implemented[/red]"