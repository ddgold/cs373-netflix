#!/usr/bin/env python3

# -------
# imports
# -------
import math
import json

# -------
# globals
# -------
ActualCache = {}
MovieCache = {}
UserCache = {}
NetAvg = 3.604289964420661

# ------------
# netflix_read
# ------------
def netflix_read (r) :
	"""
	r is a reader
	returns the next line, WITHOUT newline, as a string
	"""
	return (str(s)[:len(s) - 1] for s in r)


# ------------
# netflix_eval
# ------------
def netflix_eval (m, u) :
	"""
	m is the id of a movie
	u is the id of a user
	return accutal and predicted rating of movie m for user u
	"""
	assert(type(m) is str and m != "")
	assert(type(u) is str and u != "")

	a = ActualCache[str((m, u))]
	p = NetAvg + (MovieCache[m] - NetAvg) + (UserCache[u] - NetAvg)

	if p > 5.0 :
		p = 5.0
	if p < 1.0 :
		p = 1.0

	assert(a >= 1.0 and a <= 5.0)
	assert(p >= 1.0 and p <= 5.0)
	return (a, p)


#--------------
# netflix_print
#--------------
def netflix_print (w, s) :
	"""
	print string to writer
	w is a writer
	s is a sting
	"""
	assert(type(s) is str)
	w.write(s + "\n")


# -------------
# netflix_solve
# -------------
def netflix_solve (r, w) :
	"""
	read, eval, print loop
	r is reader
	w is writer
	"""
	global ActualCache, MovieCache, UserCache
	f = open('/u/thunt/cs373-netflix-tests/ddg625-ActualCache.json', 'r')
	ActualCache = json.load(f)
	f.close()
	f = open('/u/thunt/cs373-netflix-tests/ddg625-MovieCache.json', 'r')
	MovieCache = json.load(f)
	f.close()
	f = open('/u/thunt/cs373-netflix-tests/ddg625-UserCache.json', 'r')
	UserCache = json.load(f)
	f.close()
	
	m = ""
	i = 0
	rmse = 0
	for s in netflix_read(r) :
		if s[len(s) - 1] == ':' :
			m = (s[:len(s) - 1])
			netflix_print(w, s)
		else :
			assert (m != "")
			a, p = netflix_eval(m, s)
			rmse += (a - p) ** 2
			i += 1
			netflix_print(w, str(p))
	rmse = math.sqrt(rmse / i)
	netflix_print(w, "RMSE: " + str(rmse))


