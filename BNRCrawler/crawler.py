import requests
class Crawler:
	def __init__(self, base_url='https://bnr.bg/hristobotev/radioteatre/list'):
		self.base_url = base_url

	def get_html(self):
		r = requests.get(self.base_url)

		if r.ok:
			return r.text
		else:
			raise Exception('Server did not return OK')


	def get_publication(self):
		pass


	def start(self):
		html  = self.get_html
		self.html = html
		self.get_publication()
