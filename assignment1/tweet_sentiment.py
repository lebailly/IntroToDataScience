#!/usr/bin/env python2.7

"""
A twitter data (in json format) is read from stdin.  A sentiment file is read
with data about.
"""

import sys, json, collections, argparse

def main():

	options = parse_arguments()

	scores_dict = get_AFINN(options.sent_file)

	for tweet_str in sys.stdin:
		score = 0
		JSONObject = json.loads(tweet_str)
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

def parse_arguments():
    """ Parses arguments from comandline."""

    parser = argparse.ArgumentParser(description = __doc__)

    parser.add_argument('--sent_file', '-s', type=argparse.FileType('r'), 
    	nargs='?', default='AFINN-111.txt',
    	help='A tab-separated list of English words rated for valence.')
    parser.add_argument('--non_zero', '-z', action='store_true',
    	help='Shows only non-zero scores if selected (defaults to False).')
    parser.add_argument('--print_tweet','-t', action='store_true',
    	help='Shows tweet and score (defaults to False).')
    
    return parser.parse_args()

if __name__ == '__main__':
    main()