import requests
import os
#import sys
import urllib
#import unicodedata
#import codecs
import pickle
from subprocess import call
from random import randint
import json
import getpass

user=getpass.getuser()
url_list=[]
i=1
base_url="http://bing.com"
request_url="http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=10&mkt=en-US"
r=urllib.urlopen(request_url)
parsed_json=json.load(r)
last_date=str(parsed_json['images'][7]['startdate'])
file_exists=os.path.isfile("///home/"+user+"/.url_list.txt")
use_old_file=0

if file_exists:
	url_list = pickle.load(open("///home/"+user+"/.url_list.txt",'r'))
	if url_list[0] == last_date:
		use_old_file=1

if (file_exists == 0) or (use_old_file == 0):
	list_storage=open("url_list.txt",'w')
	url_list=[]
	url_list.append(last_date)
	while i < 8:
		current_url=parsed_json['images'][i]['url']
		url_list.append(current_url)
		i=i+1


pickle.dump(url_list,list_storage)
list_storage.close()

rand_num=randint(1,7)
wallpaper_url=base_url+url_list[rand_num]

print "-----------------Downloading-------------------"
urllib.urlretrieve(wallpaper_url,"///home/"+user+"/.dynamic-wall-bing-temp.jpg")
call(["gsettings","set","org.gnome.desktop.background","picture-uri","file:///home/"+user+"/.dynamic-wall-bing-temp.jpg"])



