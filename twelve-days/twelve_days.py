def recite(start_verse, end_verse):

	lyrics = ['twelve Drummers Drumming', 'eleven Pipers Piping', 'ten Lords-a-Leaping', 'nine Ladies Dancing', 'eight Maids-a-Milking', 'seven Swans-a-Swimming', 'six Geese-a-Laying', 'five Gold Rings', 'four Calling Birds', 'three French Hens', 'two Turtle Doves', 'and a Partridge in a Pear Tree.']
	days = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

	sing = ' day of Christmas my true love gave to me: '

	recite = []
	i = 11
	for text in lyrics.copy():
		row = 'On the ' + days[i] + sing + ', '. join(lyrics)
		if row == 'On the first day of Christmas my true love gave to me: and a Partridge in a Pear Tree.':
			row = 'On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.'
		row += '\n'
		recite.append(row)
		lyrics = lyrics[1:]
		i -= 1

	recite = recite[::-1]

	return ''.join(recite[start_verse-1: end_verse])
