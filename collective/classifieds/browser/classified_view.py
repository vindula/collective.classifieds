__author__ = """Four Digits <Ralph Jacobs>"""
__docformat__ = 'plaintext'

from Products.Five import BrowserView


class classified_view(BrowserView):
	"""
		BrowserView for classified
	"""

	def format_moeda(self, valor):
		import locale
		locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
		return  locale.currency( float(valor), grouping=True)


	def get_price(self):
		valor = self.context.price
		if valor:
			return self.format_moeda(valor)
		else:
			return 'R$ 0,00'