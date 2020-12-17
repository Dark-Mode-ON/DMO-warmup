import pytest


class TestClass:
	def test_one(self):
		assert 1 == 1

	def test_maciej_piesiak(self):
		maciej = "maciej"
		assert "maciej" == maciej

	@staticmethod
	def test_domino_nocek():
		domino = "domino"
		assert "domino" == domino
