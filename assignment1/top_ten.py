#!/usr/bin/env python2.7

"""
PROGRAM DOC 
"""

import sys, json, collections

def main():

	hash_tag_freqs = collections.Counter()

	for tweet_str in sys.stdin:
		tweet_dict = json.loads(tweet_str)
		try:
			hash_tags_list = tweet_dict['entities']['hashtags']
			for hash_tags in hash_tags_list:
				hash_tag_freqs[hash_tags['text']] += 1
		except:
			pass

	for word, freq in hash_tag_freqs.most_common(10):
		print word, freq

if __name__ == '__main__':
    main()


#Add English Only option

# tweet = tweet_dict['text']
# for word in tweet.split():
# 	if(word.startswith('#')):
# 		word = word.lstrip('#')
# 		hash_tag_freqs[word] += 1