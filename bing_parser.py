import requests
import os
import urllib
import pickle
from subprocess import call
from random import randint
import json
import getpass

def main():
	user=getpass.getuser()
	url_list=[]
	i=0
	base_url="http://bing.com"
	request_url="http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=10&mkt=en-US"
	r=urllib.urlopen(request_url)
	parsed_json=json.load(r)

	while i < 7:
		current_url=parsed_json['images'][i]['url']
		url_list.append(current_url)
		i=i+1

	rand_num=randint(0,6)
	wallpaper_url=base_url+url_list[rand_num]

	print "-----------------Downloading-------------------"
	urllib.urlretrieve(wallpaper_url,"///home/"+user+"/.dynamic-wall-bing-temp.jpg")
	call(["gsettings","set","org.gnome.desktop.background","picture-uri","file:///home/"+user+"/.dynamic-wall-bing-temp.jpg"])

if __name__ == "__main__":
	main()



