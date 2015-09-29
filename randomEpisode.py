import os, random, sys, re

x = "Series/Friends"

def pick_episode():
	episodes = []
	for y in os.listdir(x):
		episodes.append(x+'/'+y+'/'+random.choice(os.listdir(x+'/'+y)))

	picked = random.choice(episodes)
	
	while  re.match('^[.srt]$', picked) != None:
		pick_episode()
	
	return picked

path = pick_episode()

path = path.replace(" ", "\ ")
path = path.replace("\'", "\\\'")
index = path.rfind("/")

name = path[index+1:]
path = path[:index]

os.chdir(path)
os.system('vlc ' + name)

	
	
		


