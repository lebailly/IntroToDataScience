from __future__ import division
import sys, json, collections

def main():

	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])

	scores_dict = get_AFINN(sent_file)

	happiness = collections.defaultdict(list)

	for tweet_str in tweet_file:
		score = 0
		tweet_dict = json.loads(tweet_str)
		if('place' in tweet_dict.keys() and tweet_dict['place'] is not None): #ATTEN - can I do this with try?
			if(tweet_dict['place']['country_code'] == 'US'):
				state = tweet_dict["place"]["full_name"].split(',')[-1].strip()
				if(state != 'USA' and 'text' in tweet_dict.keys()):
					tweet = tweet_dict['text']
					for word in tweet.split():
						score += scores_dict[word]
					happiness[state].append(score)

	max_score = -10
	for state, score in happiness.items():
		if(sum(score)/len(score) > max_score): happy_state = state

	print happy_state

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

	return scores

if __name__ == '__main__':
    main()