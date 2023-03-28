import requests  
import webbrowser
def shorten_url(url):
	base_url = 'http://tinyurl.com/api-create.php?url='
	url = base_url + url
	print('Given URL', url)
	lol = requests.get(url)
	print("Shorten URL:",lol.text)
	n=int(input("Enter 1 to open link:"))
	if(n==1):
		webbrowser.open(lol.text)
url =input("Enter long URL:")
shorten_url(url)