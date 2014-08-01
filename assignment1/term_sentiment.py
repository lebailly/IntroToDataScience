#!/usr/bin/env python2.7

"""
PROGRAM DOC 
"""

from __future__ import division
import sys, json, collections, argparse

def main():

	options = parse_arguments()

	scores_dict = get_AFINN(options.sent_file)
	sent_words = scores_dict.keys()
	new_words = collections.defaultdict(list)

	for tweet_str in sys.stdin:
		score = 0
		JSONObject = json.loads(tweet_str)
		try:
			if(JSONObject['lang'] == 'en'):
				tweet = JSONObject['text']
				for word in tweet.split():
					score += scores_dict[word]
				for word in tweet.split():
					if(word not in sent_words): new_words[word].append(score)
		except:
			pass
				
	for word, scores in new_words.items():
		print word, sum(scores)/len(scores)


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
    
    return parser.parse_args()
    
if __name__ == '__main__':
    main()