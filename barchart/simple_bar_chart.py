from .. import chart_template
from rich import color

class SimpleBarChart(chart_template.simple_chart.SimpleChart):
	def graph(self):
		self.margin['l'] = 5

		w = (self.w-2-self.margin['l']-self.margin['r'])
		h = (self.h-4)
		s = []
		label = []

		factor = (max(self.data)-min(self.data)+2)/h
		offset = -min(self.data)/factor+1
		for y in range(h):
			l = ""
			for ind, i in enumerate(self.data):
				c = '█' if (h-y) < i/factor+offset else ('▄' if (h-y) == i/factor+offset else ' ')
				l += f" [{self.colors[ind]}]{c*int(w//len(self.data)-2)}[/{self.colors[ind]}] "
			label= '{:0>5.2f}'.format((h-y-offset)*factor)
			s.append([label if y%3 == 0 else " "*5, l])
		return s