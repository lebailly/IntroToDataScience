#!/usr/bin/env python2.7

"""
A twitter data (in JSON format) is read from stdin.  A sentiment file 
(--sent_file) is read in, giving a set of words integer scores from -5 (the most
negative) to +5 (the most positive).  Tweets which are in English are then given
a score which is the sum of the score of words in --sent_file.  Any words not
found are given a score of zero.  Scores are printed to stdout, with options
to print the tweet (-t) and also only print non-zero tweets (-z).
"""

import sys, json, collections, argparse

def main():
	"""
	Parses arguments from the command line, loads the sentiment file into a
	dictionary, then reads tweets and scores them.
	"""

	options = parse_arguments()

	#scores_dict[word] = score where -5 <= score <= 5.
	scores_dict = get_AFINN(options.sent_file)

	for tweet_str in sys.stdin:
		score = 0
		JSONObject = json.loads(tweet_str) #Dict with attributes from JSON entry
		try:
			if(JSONObject['lang'] == 'en'):
				tweet = JSONObject['text']
				for word in tweet.split():
					score += scores_dict[word]
				if((options.non_zero and score != 0) or not options.non_zero): 
					print score
					if(options.print_tweet): 
						print '\n', tweet, '\n\n\n***************************\n'
		except:
			pass

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
    parser.add_argument('--positive', '-p', action='store_true',
    	help='Shows only non-zero scores if selected (defaults to False).')
    parser.add_argument('--print_tweet','-t', action='store_true',
    	help='Shows tweet (defaults to False).')
    
    return parser.parse_args()

if __name__ == '__main__':
    main()