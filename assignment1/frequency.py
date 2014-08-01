#!/usr/bin/env python2.7

"""
PROGRAM DOC 
"""

import sys, json, collections, argparse

def main():

	# options = parse_arguments()

	word_freqs = collections.Counter()

	for tweet_str in sys.stdin:
		JSONObject = json.loads(tweet_str)
		try:
			tweet = JSONObject['text']
			for word in tweet.split():
				word_freqs[word] += 1
		except:
			pass

	for word, freq in word_freqs.items():
		print word, freq

#ATTEN - Add normlization?  Make an Argparse option?
#ADD TOP TEN (OR TOP option) filter?
#ADD SORT OPTIONS?
#Add Englih only option

# def parse_arguments():
#     """ Parses arguments from comandline."""

#     parser = argparse.ArgumentParser(description = __doc__)

#     parser.add_argument('--sent_file', '-s', type=argparse.FileType('r'), 
#     	nargs='?', default='AFINN-111.txt',
#     	help='A tab-separated list of English words rated for valence.')
    
#     return parser.parse_args()

if __name__ == '__main__':
    main()