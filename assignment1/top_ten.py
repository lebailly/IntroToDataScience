#!/usr/bin/env python2.7

"""
top_ten.py determines the top ten hash tags.  Tweets are read (in json) from
stdin. The top 10 are printed to stdout along with their frequency (count).
"""

import sys, json, collections

def main():
	"""
	Tweets are read (in json) from stdin.  A list of hash tags is produced 
	(if possible).  After all tweets are read, the top 10 are printed to stdout 
	along with their frequency (count).
	"""

	#hash_tag_freqs[x] = number of times x found in 'entities':'hashtags'
	hash_tag_freqs = collections.Counter()

	for tweet_str in sys.stdin:
		JSONObject = json.loads(tweet_str) #Dict with attributes from JSON entry
		try:
			hash_tags_list = JSONObject['entities']['hashtags']
			for hash_tags in hash_tags_list:
				hash_tag_freqs[hash_tags['text']] += 1
		except:
			pass

	for word, freq in hash_tag_freqs.most_common(10):
		print word, freq

if __name__ == '__main__':
    main()

# tweet = JSONObject['text']
# for word in tweet.split():
# 	if(word.startswith('#')):
# 		word = word.lstrip('#')
# 		hash_tag_freqs[word] += 1