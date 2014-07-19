import sys, json, collections

def main():
	
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])

	scores_dict = get_AFINN(sent_file)

	for tweet_str in tweet_file:
		score = 0
		tweet_dict = json.loads(tweet_str)
		if('text' in tweet_dict.keys()): #ATTEN - can I do this with try?
			tweet = tweet_dict['text']
			for word in tweet.split():
				score += scores_dict[word]
		print score

def get_AFINN(sent_file):
	"""
	Pre-condition: fname is a path to a file.  Each line in the file contains a 
	word or phrase followed by a sentiment score, which are tab-delimited.

	Post-condition: Returns a collections.Counter() with a word as a key and its 
	sentiment score as the value.
	"""

	scores = collections.Counter() # initialize an empty dictionary

	for line in sent_file:
		term, score  = line.split("\t")  # The file is tab-delimited.
		scores[term] = int(score)  # Convert the score to an integer.

	#print scores.items() # Print every (term, score) pair in the dictionary

	return scores

if __name__ == '__main__':
    main()