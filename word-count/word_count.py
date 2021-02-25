import re

def count_words(sentence):
	sentence = sentence.lower().replace('_', ' ')
	words = re.findall(r'\b\"?\w+\'?\w{,2}\"?\b', sentence)
	return {f'{word}': words.count(word) for word in words}
