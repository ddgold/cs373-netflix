#!/usr/bin/env python3

# -------
# imports
# -------
import math

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
	assert(m > 0)
	assert(u > 0)

	# Eval Here
	p = 1.0
	a = 2.0
	assert(a >= 0.0 and a <= 5.0)
	assert(p >= 0.0 and p <= 5.0)
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
	m = 0
	i = 0
	rmse = 0
	for s in netflix_read(r) :
		if s[len(s) - 1] == ':' :
			m = int(s[:len(s) - 1])
			netflix_print(w, s)
		else :
			assert (m > 0)
			a, p = netflix_eval(m, int(s))
			rmse += (a - p) ** 2
			i += 1
			netflix_print(w, str(p))
	rmse = math.sqrt(rmse / i)
	netflix_print(w, "RMSE: " + str(rmse))