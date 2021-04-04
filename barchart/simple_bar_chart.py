from .. import chart_template
from rich import color

class SimpleBarChart(chart_template.simple_chart.SimpleChart):
	def graph(self):
		self.margin['l'] = 5

		w = (self.w-2-self.margin['l']-self.margin['r'])
		h = (self.h-4)
		s = []
		label = []

		sep = self.separator
		sep_style = self.separator_style
		sep_str = f'[{sep_style}]{sep}[/{sep_style}]' if sep_style else sep

		factor = (max(self.data)-min(self.data)+1)/h
		offset = -min(self.data)/factor+2
		for y in range(h):
			rl = " "
			l = " "
			for ind, i in enumerate(self.data):
				c = '█' if (h-y) < i/factor+offset else ('▄' if (h-y) == i/factor+offset else ' ')
				rl += f"{sep if ind != 0 else ''}{c*int(w//len(self.data)-len(sep))}"
				l += f"{sep_str if ind != 0 else ''}[{self.colors[ind]}]{c*int(w//len(self.data)-len(sep))}[/{self.colors[ind]}]"
			label= '{:0>5.1f}'.format((h-y-offset)*factor)
			s.append([label if y%3 == 0 else " "*5, rl+" ", l+" "])
		return s