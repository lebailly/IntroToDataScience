#!/usr/bin/env python2.7

"""
PROGRAM DOC 
"""

from __future__ import division
import sys, json, collections, argparse

#Add options to determin location in different ways (some can use internet).
#Add option to print happiest state, or list of all states and scores

def main():

	options = parse_arguments()

	scores_dict = get_AFINN(options.sent_file)
	happiness = collections.defaultdict(list)

	for tweet_str in sys.stdin:
		score = 0
		JSONObject = json.loads(tweet_str)
		try:
			if(JSONObject['place']['country_code'] == 'US'):
				state = JSONObject["place"]["full_name"].split(',')[-1].strip()
				if(state != 'USA' and JSONObject['lang'] == 'en'):
					tweet = JSONObject['text']
					for word in tweet.split():
						score += scores_dict[word]
					happiness[state].append(score)
		except:
			pass

	max_score = -10

	if(len(happiness) == 0):
		happy_state = None
		sys.stderr.write('There are not enough tweets to preform this analysis!\n')
	else:
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

def parse_arguments():
    """ Parses arguments from comandline."""

    parser = argparse.ArgumentParser(description = __doc__)

    parser.add_argument('--sent_file', '-s', type=argparse.FileType('r'), 
    	nargs='?', default='AFINN-111.txt',
    	help='A tab-separated list of English words rated for valence.')
    
    return parser.parse_args()
if __name__ == '__main__':
    main()