"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 11
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 7


def one_to_six(dice, category):
	score = dice.count(category) * category
	return score

def score(dice, category):
	if category in [1, 2, 3, 4, 5, 6]:
		return one_to_six(dice, category)
	
	if category == 0:
		if len(list(set(dice))) == 1:
			return 50
		else:
			return 0

	if category == 7:
		return sum(dice)

	if category == 8:
		tmp = list(set(dice))
		if len(tmp) == 1:
			return tmp[0] * 4
		if len(tmp) == 2:
			if dice.count(tmp[0]) == 4:
				return tmp[0] * 4
			elif dice.count(tmp[1]) == 4:
				return tmp[1] * 4
			else:
				return 0

	if category == 9:
		tmp = list(set(dice))
		if sorted(tmp) == [1, 2, 3, 4, 5]:
			return 30
		else:
			return 0

	if category == 10:
		tmp = list(set(dice))
		if sorted(tmp) == [2, 3, 4, 5, 6]:
			return 30
		else:
			return 0
	
	if category == 11:
		tmp = list(set(dice))
		if len(tmp) == 2:
			if (dice.count(tmp[0]) == 2 and dice.count(tmp[1]) == 3) or (dice.count(tmp[0]) == 3 and dice.count(tmp[1]) == 2):
				return sum(dice)
			else:
				return 0
		else:
			return 0