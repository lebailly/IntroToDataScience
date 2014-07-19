import sys, json, collections

def main():

	hash_tag_freqs = collections.Counter()
	
	tweet_file = open(sys.argv[1])

	for tweet_str in tweet_file:
		tweet_dict = json.loads(tweet_str)
		if('entities' in tweet_dict.keys()): #ATTEN - can I do this with try?
			hash_tags_list = tweet_dict['entities']['hashtags']
			for hash_tags in hash_tags_list:
				hash_tag_freqs[hash_tags['text']] += 1

	for word, freq in hash_tag_freqs.most_common(10):
		print word, freq

if __name__ == '__main__':
    main()



# tweet = tweet_dict['text']
# for word in tweet.split():
# 	if(word.startswith('#')):
# 		#word = word.lstrip('#')
# 		hash_tag_freqs[word] += 1