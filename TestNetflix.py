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

from Netflix.py import netflix_read, netflix_eval, netflix_print, netflix_solve

# -----------
# TestNetflix
# -----------

class TestNetflix (unittest.TestCase) :
	# ----
	# read
	# ----
	def test_read_1 (self) :
		r = io.StringIO("2043:")
		s = netflix_read(r)
		self.assertTrue(s == "2043:")

	def test_read_2 (self) :
		r = io.StringIO("3.4")
		s = netflix_read(r)
		self.assertTrue(s == "3.4")

	def test_read_3 (self) :
		r = io.StringIO("")
		s = netflix_read(r)
		self.assertTrue(s == "")


	# ----
	# eval
	# ----
	def test_eval_1 (self) :
		v = netflix_eval(2043, 1417435)
		self.assertTrue(v >= 0.0 and v <= 5.0)

	def test_eval_2 (self) :
		v = netflix_eval(2043, 2312054)
		self.assertTrue(v >= 0.0 and v <= 5.0)

	def test_eval_3 (self) :
		v = netflix_eval(10851, 2312054)
		self.assertTrue(v >= 0.0 and v <= 5.0)


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
		netflix_print(w, "RNSE: 0.95")
		self.assertTrue(w.getvalue() == "RNSE: 0.95\n")

	# -----
	# solve
	# -----
	def test_solve_1 (self) :
		r = io.StringIO("2043:\n1417435\n2312054\n462685\n")
		w = io.StringIO()
		netflix_solve(r, w)
		self.assertTrue(w.getvalue() == "2043:\n3.4\n4.1\n1.9\nRMSE: 0.95\n")

	def test_solve_2 (self) :
		r = io.StringIO("2043:\n1417435\n2312054\n462685\n")
		w = io.StringIO()
		netflix_solve(r, w)
		self.assertTrue(w.getvalue() == "2043:\n3.4\n4.1\n1.9\nRMSE: 0.95\n")

	def test_solve_3 (self) :
		r = io.StringIO("2043:\n1417435\n2312054\n462685\n")
		w = io.StringIO()
		netflix_solve(r, w)
		self.assertTrue(w.getvalue() == "2043:\n3.4\n4.1\n1.9\nRMSE: 0.95\n")


# ----
# main
# ----
print("TestNetflix.py")
unittest.main()
print("Done.")