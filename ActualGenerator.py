import sys
import json

def findMovie(m) :
	assert (int(m) > 0)
	x = 7 - len(m)
	s = "/u/downing/cs/netflix/training_set/mv_"
	for i in range(x) :
		s += "0"
	s += m + ".txt"
	assert (len(s) == 49)
	return s

def findUser(m, u) :
	f = open(m, "r")
	f.readline()
	for line in f :
		x = line.split(',')
		if x[0] == u :
			return float(x[1])
	assert (False)

def buildActual() :
	f = open("/u/downing/cs/netflix/probe.txt", encoding = "ISO-8859-1")
	cache = {}
	m = ""
	for line in f :
		if line[len(line) - 2] == ":" :
			m = line[:len(line) - 2]
		else :
			assert (m != "")
			u = line[:len(line) - 1]
			cache[(str((m, u)))] = findUser(findMovie(m), u)
	return cache


def buildUser() :
	f = open("/u/downing/cs/netflix/movie_titles.txt", encoding = "ISO-8859-1")
	cache = {}
	for line in f :
		x = line.split(",")
		m = findMovie(x[0])
		f2 = open(m, "r")
		f2.readline()
		for line2 in f2 :
			y = line2.split(",")
			if cache.get(y[0]) == None :
				cache[y[0]] = [0, 0]
			cache[y[0]][0] += int(y[1])
			cache[y[0]][1] += 1
	for key, value in cache.items() :
		cache[key] = value[0] / value[1]
	return cache

def buildMovie () :
	f = open("/u/downing/cs/netflix/movie_titles.txt", encoding = "ISO-8859-1")
	cache = {}
	for line in f :
		x = line.split(",")
		m = findMovie(x[0])
		f2 = open(m, "r")
		f2.readline()
		cache[x[0]] = [0,0]
		for line2 in f2 :
			y = line2.split(",")
			cache[x[0]][0] += int(y[1])
			cache[x[0]][1] += 1
	for key, value in cache.items() :
			cache[key] = value[0]/value[1]
	return cache

def buildCache (cache):
	if cache == 0 or cache == 1 :
		print ("MovieCache Started...")
		movies = buildMovie()
		with open('MovieCache.json', 'w') as f:
			json.dump(movies, f)
		print ("MovieCache Done.")
	if cache == 0 or cache == 2 :
		print ("UserCache Started...")
		users = buildUser()
		with open('UserCache.json', 'w') as f:
			json.dump(users, f)
		print ("UserCache Done.")
	if cache == 0 or cache == 3 :
		print ("ActualCache Started...")
		actual = buildActual()
		with open('ActualCache.json', 'w') as f:
			json.dump(actual, f)
		print ("ActualCache Done.")


print (sys.argv[0])
if len(sys.argv) > 1 :
	buildCache(int(sys.argv[1]))
else :
	buildCache(0)