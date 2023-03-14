import collections

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck(object):
	"""
	同时实现__len__和__getitem__，FrenchDeck就像一个Python自有的序列数据类型一样；
	例如迭代和切片。
	"""
	ranks = [str(n) for n in range(2, 11)] + list("JQKA")
	suits = "spades diamonds clubs hearts".split()

	def __init__(self):
		self._cards = [Card(rank, suit) for suit in self.suits
			for rank in self.ranks]

	def __len__(self):
		return len(self._cards)

	def __getitem__(self, position):
		return self._cards[position]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
	rank_value = FrenchDeck.ranks.index(card.rank)
	return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == "__main__":
	deck = FrenchDeck()
	print(len(deck))

	print(deck[0])
	print(deck[-1])

	from random import choice
	print(choice(deck))
	print(choice(deck))

	print(deck[:3])

	for card in deck:
		print(card)

	for card in reversed(deck):
		print(card)

	# 给卡牌排序
	for card in sorted(deck, key=spades_high):
		print(card)
	# TODO: 如何洗牌？11章会讲。

