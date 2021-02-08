def is_pangram(sentence):
	alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
	sentence = sentence.lower()
	li = set([i for i in sentence if i not in ['.', ' ', ',','_','1','2','3','4','5','6','7','8','9','0','\"']])
	if sorted(li) == sorted(alphabet):
		return True
	return False
