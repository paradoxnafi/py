import random
import urllib.request

def image_downloader():
	print("Enter url: ")
	url = input()
	name = random.randrange(1000, 9999)
	fullname = str(name) + '.jpg'
	urllib.request.urlretrieve(url, fullname)

image_downloader()