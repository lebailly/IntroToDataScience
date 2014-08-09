#!/usr/bin/env python2.7

"""
happiest_state determines the happiest state of the tweets read (in JSON) from
stdin.  Tweets are scored using the method described in the twee_sentiment.py
doc string.  The location is determined using "place":"full_name" attribute.
Many tweets will not have this information; these are ignored.  The scores
are recorded by state and averaged.  The abbreviation for the state with the 
highest score is printed to stdout.
"""

from __future__ import division
import sys, json, collections, argparse

def main():
	"""
	Parses command line arguments, loads a sentiment dictionary, scores tweets
	read from stdin (in JSON format) that have 'place':'country_code' == 'US'
	and have a 'place':'full_name' attribute.  These tweets are scored and
	stored by state.  The state with the highest average is printed to stdout.
	"""

	options = parse_arguments()

	#scores_dict is a dictionary.  scores_dict[word] = score, where 
	#-5 <= score <= 5 ratting how positive or negative word is.
	scores_dict = get_AFINN(options.sent_file)

	#happiness[state] = list of scores (which is averaged at the programs end)
	happiness = collections.defaultdict(list)

	for tweet_str in sys.stdin:
		score = 0
		JSONObject = json.loads(tweet_str) #Dict with attributes from JSON entry
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
		sys.stderr.write('''There are not enough tweets to preform 
							this analysis!\n''')
	else:
		for state, score in happiness.items():
			if(sum(score)/len(score) > max_score): happy_state = state

	print happy_state

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