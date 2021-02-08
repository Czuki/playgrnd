import datetime

def add(moment):
	delta = datetime.timedelta(seconds=1000000000)
	result = moment + delta
	return result

