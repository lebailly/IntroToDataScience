import sys, json, collections

def main():

	word_freqs = collections.Counter()
	
	tweet_file = open(sys.argv[1])

	for tweet_str in tweet_file:
		tweet_dict = json.loads(tweet_str)
		if('text' in tweet_dict.keys()): #ATTEN - can I do this with try?
			tweet = tweet_dict['text']
			for word in tweet.split():
				word_freqs[word] += 1

	for word, freq in word_freqs.items():
		print word, freq

#ATTEN - Add normlization?  Make an Argparse option?

if __name__ == '__main__':
    main()