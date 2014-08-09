#!/usr/bin/env python2.7

"""
frequency.py determines the frequency of different words found in tweets.
Tweets are read (in JSON format) from stdin.  Frequency is measured simply
as a count (it is not normalized).  The word and frequency is printed to stdout. 
"""

import sys, json, collections, argparse

def main():
	"""
	Reads tweets from stdin, counts frequency of different words.
	"""
	
	#word_freqs[word] = number of occurrences of word in tweets from stdin.
	word_freqs = collections.Counter()

	for tweet_str in sys.stdin:
		JSONObject = json.loads(tweet_str) #Dict with attributes from JSON entry
		try:
			tweet = JSONObject['text']
			for word in tweet.split():
				word_freqs[word] += 1
		except:
			pass

	for word, freq in word_freqs.items():
		print word, freq

if __name__ == '__main__':
    main()