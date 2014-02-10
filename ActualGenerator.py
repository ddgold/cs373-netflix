import sys
import json

def openMovie(m) :
	x = 7 - len(m)
	s = "/u/downing/cs/netflix/training_set/mv_"
	for i in range(x) :
		s += "0"
	s += m + ".txt"
	return s

def findUser(m, u) :
	f = open(m, "r")
	f.readline()
	for line in f :
		x = line.split(',')
		if x[0] == u :
			return x[1]

def readFile(r) :
	return (str(s)[:len(s) - 1] for s in r)

def buildActual() :
	m = ""
	for x in (readFile(sys.stdin)) :
		if (x[len(x) - 1] == ":") :
			m = openMovie(x[:len(x) - 1])
		else :
			print(str(findUser(m, x)))

def buildUser() :
	f = open("/u/downing/cs/netflix/movie_titles.txt", encoding = "ISO-8859-1")
	cache = {}
	for line in f :
		x = line.split(",")
		m = openMovie(x[0])
		f2 = open(m, "r")
		f2.readline()
		for line2 in f2 :
			y = line2.split(",")
			if cache.get(y[0]) == None :
				cache[y[0]] = [0, 0]
			cache[y[0]][0] += int(y[1])
			cache[y[0]][1] += 1
	return cache

def buildMovie () :
	f = open("/u/downing/cs/netflix/movie_titles.txt", encoding = "ISO-8859-1")
	cache = {}
	for line in f :
		x = line.split(",")
		m = openMovie(x[0])
		f2 = open(m, "r")
		f2.readline()
		cache[x[0]] = [0,0]
		for line2 in f2 :
			y = line2.split(",")
			cache[x[0]][0] += int(y[1])
			cache[x[0]][1] += 1
	return cache

def buildCache ():
	movies = buildMovie()
	users = buildUser()
	combo = {}
	m = 0
	for x in (readFile(sys.stdin)) :
		if (x[len(x) - 1] == ":") :
			m = int(x[:len(x) - 1])
		else :
			assert(m > 0)
			u = int(x)
			combo[str((m, u))] = (movies[str(m)][0] / movies[str(m)][1] + users[str(u)][0] / users[str(u)][1]) / 2
	with open('Cache.json', 'w') as f:
		json.dump(combo, f)

buildCache()
