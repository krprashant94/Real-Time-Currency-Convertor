import requests
import re

def convert(form, to):
	"""
	:param to str: to currecy
	:param from str: from currency
	:raise: AttributeError if currency not found or URL change
	"""
	s = requests.Session()
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	# URL to open
	open_url = 'https://www.google.co.in/search?q='+str(form)+'+to+'+str(to)
	r = s.get(open_url, headers=headers)
	# regular expression may change time to time
	m = re.search('id="knowledge-currency__tgt-amount"\>(.*?)<\/span>', r.text)
	return m.group(1)

if __name__ == '__main__':
	print(convert('usd', 'inr'))