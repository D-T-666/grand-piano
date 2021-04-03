from ..terminal_size import get_terminal_size
from random import randint
from rich.measure import Measurement

class SimpleChart:
	def __init__(self, name=""):
		self.name = name
		self.w, self.h = get_terminal_size()
		self.margin = {
			't': 0,
			'r': 0,
			'b': 0,
			'l': 0
		}

		self.colors = [f'rgb({randint(64,255)},{randint(64,255)},{randint(64,255)})' for i in range(100)]

	def __str__(self):
		return self.render()

	def render(self):
		g = self.graph()
		w = (self.w-2-self.margin['r']-self.margin['l'])
		s = f"{' '*self.margin['l']}┏{'━'*w}┓"
		s += "\n".join([f"{label}┃{a}{'&'*(w-len(a))}┃" for label, a in g])+"\n"
		s += f"{' '*self.margin['l']}┗{'━'*w}┛"
		s += str(self.name)
		return s

	def plot(self, data):
		self.data = data

	def graph(self):
		return " ", "[red]graph() function has not been implemented[/red]"