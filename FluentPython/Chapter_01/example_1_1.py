import collections

Card = collections.namedtuple("Card", ["rank", "suit"])

class FrenchDeck(object):
	ranks = [str(n) for n in range(2, 11)] + list("JQKA")
	suits = "spades diamonds clubs hearts".split()

