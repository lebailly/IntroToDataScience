#!/usr/bin/env python2.7

"""
term_sentiment generates a sentiment score for words not found in the sentiment
file (--sent_file).  A score is generated for each tweet read from stdin (in
JSON format) where words not found in --sent_file are have score 0.  This score
is then recorded for each word not found in the sentiment file.  This is 
repeated for all tweets in stdin.  A score for each word is computed as the 
average of the recorded scores.  The new words and scores are printed to stdout, 
tab-separated.
"""

from __future__ import division, print_function
import sys, json, collections, argparse

def main():

	options = parse_arguments()

	#scores_dict is a dictionary.  scores_dict[word] = score, where 
	#-5 <= score <= 5 ratting how positive or negative word is.
	scores_dict = get_AFINN(options.sent_file)

	#sent_words is a list of words in the scoers_dict (stored since used often)
	sent_words = scores_dict.keys()

	#new_words_scores[word] is the sum of the scores for the tweets which
	#contain the word.  new_words_counts is the number of times the word occurs.
	#Only words which are not in sent_words are stored here.
	new_word_scores = collections.Counter()
	new_word_counts = collections.Counter()

	for tweet_str in sys.stdin:
		score = 0
		JSONObject = json.loads(tweet_str) #Dict with attributes from JSON entry
		try:
			if(JSONObject['lang'] == 'en'):
				tweet = JSONObject['text']
				for word in tweet.split():
					score += scores_dict[word]
				for word in tweet.split():
					if(word not in sent_words): 
						new_word_scores[word] += score
						new_word_counts[word] += 1
		except:
			pass
				
	for word, total_score in new_word_scores.items():
		print(word, '\t', total_score/new_word_counts[word],sep='')


def get_AFINN(sent_file):
	"""
	Pre-condition: sent_file is a path to a file.  Each line in the file 
	contains a word or phrase followed by a sentiment score, which are 
	tab-delimited.

	Post-condition: Returns a collections.Counter() with a word as a key 
	and its sentiment score as the value.
	"""

	scores = collections.Counter() # initialize an empty dictionary

	for line in sent_file:
		term, score  = line.split("\t")  # The file is tab-delimited.
		scores[term] = int(score)  # Convert the score to an integer.

	return scores

def parse_arguments():
    """ Parses arguments from command line."""

    parser = argparse.ArgumentParser(description = __doc__)

    parser.add_argument('--sent_file', '-s', type=argparse.FileType('r'), 
    	nargs='?', default='AFINN-111.txt',
    	help='A tab-separated list of English words rated for valence.')
    
    return parser.parse_args()

if __name__ == '__main__':
    main()