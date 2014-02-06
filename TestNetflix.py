#!/usr/bin/env python3

"""
To test the program:
% python TestCollatz.py >& TestCollatz.out
% chmod ugo+x TestCollatz.py
% TestCollatz.py >& TestCollatz.out
"""

# -------
# imports
# -------

import io
import unittest

from Netflix import netflix_read, netflix_eval, netflix_print, netflix_solve

# -----------
# TestNetflix
# -----------

class TestNetflix (unittest.TestCase) :
	# ----
	# read
	# ----
	def test_read_1 (self) :
		r = io.StringIO("2043:\n")
		s = next(netflix_read(r))
		self.assertTrue(str(s) == "2043:")

	def test_read_2 (self) :
		r = io.StringIO("3.4\n")
		s = next(netflix_read(r))
		self.assertTrue(str(s) == "3.4")

	def test_read_3 (self) :
		r = io.StringIO("\n")
		s = next(netflix_read(r))
		self.assertTrue(str(s) == "")

	# ----
	# eval
	# ----
	def test_eval_1 (self) :
		a, p = netflix_eval(2043, 1417435)
		self.assertTrue(a >= 1.0 and a <= 5.0)
		self.assertTrue(p >= 1.0 and p <= 5.0)

	def test_eval_2 (self) :
		a, p = netflix_eval(2043, 1417435)
		self.assertTrue(a >= 1.0 and a <= 5.0)
		self.assertTrue(p >= 1.0 and p <= 5.0)

	def test_eval_3 (self) :
		a, p = netflix_eval(2043, 1417435)
		self.assertTrue(a >= 1.0 and a <= 5.0)
		self.assertTrue(p >= 1.0 and p <= 5.0)


	# -----
	# print
	# -----
	def test_print_1 (self) :
		w = io.StringIO()
		netflix_print(w, "12:")
		self.assertTrue(w.getvalue() == "12:\n")

	def test_print_2 (self) :
		w = io.StringIO()
		netflix_print(w, "2.4")
		self.assertTrue(w.getvalue() == "2.4\n")

	def test_print_3 (self) :
		w = io.StringIO()
		netflix_print(w, "RMSE: 0.95")
		self.assertTrue(w.getvalue() == "RMSE: 0.95\n")

	# -----
	# solve
	# -----
	def test_solve_1 (self) :
		r = io.StringIO("2043:\n1417435\n2312054\n462685\n")
		w = io.StringIO()
		netflix_solve(r, w)
		s = w.getvalue()
		x = str(s).split()
		self.assertTrue(x[0] == "2043:")
		self.assertTrue(float(x[1]) >= 1.0 and float(x[1]) <= 5.0)
		self.assertTrue(float(x[2]) >= 1.0 and float(x[2]) <= 5.0)
		self.assertTrue(float(x[3]) >= 1.0 and float(x[3]) <= 5.0)
		self.assertTrue(x[4] == "RMSE:")

	def test_solve_2 (self) :
		r = io.StringIO("10851:\n1417435\n2312054\n462685\n")
		w = io.StringIO()
		netflix_solve(r, w)
		s = w.getvalue()
		x = str(s).split()
		self.assertTrue(x[0] == "10851:")
		self.assertTrue(float(x[1]) >= 1.0 and float(x[1]) <= 5.0)
		self.assertTrue(float(x[2]) >= 1.0 and float(x[2]) <= 5.0)
		self.assertTrue(float(x[3]) >= 1.0 and float(x[3]) <= 5.0)
		self.assertTrue(x[4] == "RMSE:")

	def test_solve_3 (self) :
		r = io.StringIO("2043:\n1417435\n2312054\n462685\n")
		w = io.StringIO()
		netflix_solve(r, w)
		s = w.getvalue()
		x = str(s).split()
		self.assertTrue(x[0] == "2043:")
		self.assertTrue(float(x[1]) >= 1.0 and float(x[1]) <= 5.0)
		self.assertTrue(float(x[2]) >= 1.0 and float(x[2]) <= 5.0)
		self.assertTrue(float(x[3]) >= 1.0 and float(x[3]) <= 5.0)
		self.assertTrue(x[4] == "RMSE:")


# ----
# main
# ----
print("TestNetflix.py")
unittest.main()
print("Done.")
