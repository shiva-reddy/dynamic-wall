import requests
import os
import sys
import urllib
import unicodedata
import codecs
from bs4 import BeautifulSoup
from subprocess import call
from random import randint
import getpass

def main():
	user=getpass.getuser()
	home_url="http://www.hdwallpapers.in"
	choice_list=[]
	choice_list.append("/nature__landscape-desktop-wallpapers.html")
	choice_list.append("/3d__abstract-desktop-wallpapers.html")
	choice_list.append("/animals__birds-desktop-wallpapers.html")
	choice_list.append("/anime-desktop-wallpapers.html")
	choice_list.append("/bikes__motorcycles-desktop-wallpapers.html")
	choice_list.append("/brands__logos-desktop-wallpapers.html")
	choice_list.append("/cars-desktop-wallpapers.html")
	choice_list.append("/christmas-desktop-wallpapers.html")
	choice_list.append("/digital_universe-desktop-wallpapers.html")
	choice_list.append("/dual_monitor-desktop-wallpapers.html")
	choice_list.append("/flowers-desktop-wallpapers.html")
	choice_list.append("/games-desktop-wallpapers.html")
	choice_list.append("/love-desktop-wallpapers.html")
	choice_list.append("/movies-desktop-wallpapers.html")
	choice_list.append("/others-desktop-wallpapers.html")
	choice_list.append("/photography-desktop-wallpapers.html")
	choice_list.append("/travel__world-desktop-wallpapers.html")
	choice_list.append("/vector__designs-desktop-wallpapers.html")
	i=1
	for item in choice_list:
		print str(i)+":"+item[1:-24]
		i=i+1

	choice=input()
	chosen_url=home_url+choice_list[choice-1]
	download_url="http://www.hdwallpapers.in/download"

	r=requests.get(chosen_url)
	soup=BeautifulSoup(r.content)

	image_list=[]
	i=0
	for link in soup.find_all("div",class_='thumb'):
		image_link=link.a.get("href").encode()
		image_link=download_url+image_link[:-15]+"1366x768.jpg"
		image_list.append(image_link)
		i=i+1

	print "-----------------Downloading-------------------"
	rand=randint(0,i-1)
	urllib.urlretrieve(image_list[rand],"///home/"+user+"/.dynamic-wall-hd_wall.jpg")
	call(["gsettings","set","org.gnome.desktop.background","picture-uri","file:///home/"+user+"/.dynamic-wall-hd_wall.jpg"])
	print "Done!"

if __name__ == "__main__":
    main()
