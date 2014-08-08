# Description

These programs collect current information from twitter and preform a few different types of basic analysis. This project started as part of a Coursera course on Data Science, however I have expanded upon it in several ways.

# `twitterstream.py`

## About

Used to feetch live stream data from twitter.  

## Set Up

Requires oauth2.  Must create a file name `login.txt` which contains:
api_key <api key>
api_secret <api secret>
token_key <token key>
token_secret <token secret>

See `login_example.txt' for an example.  To get credentials:

-   Create a twitter account if you do not already have one.
-   Go to https://dev.twitter.com/apps and log in with your twitter
    credentials.
-   Click "create an application"
-   Fill out the form and agree to the terms. Put in a dummy website if
    you don't have one you want to use.
-   On the next page, scroll down and click "Create my access token"
-   Copy your "Consumer key" and your "Consumer secret" into
    twitterstream.py
-   Click "Create my access token." You can [Read more about Oauth
    authorization.](https://dev.twitter.com/docs/auth)
-   Open twitterstream.py and set the variables corresponding to the
    consumer key, consumer secret, access token, and access secret
-   Run the following and make sure you see data flowing.

## Usage

Running `./twitterstream.py` will fetch a twitter stream and print the stream (in json format) to stdout for 1 minute.  Use `-t` to specify the run time or use `-u` to run for an unlimited length of time.

# `tweet_sentiment.py`

## About

Creates a numeric score rating if the tweet has a positive or negative sentiment.  This is done by using a dictionary which assigns numeric scores to individual words.  The score given to the tweet is the sum of the scores of the words (words not found in the dictionary are scored zero).

## Usage

Running `./tweet_sentiment.py` requires twitter data (in json format) in stdin.  This can be pipped with `twitterstream.py` or run using saved data.  Prints the scores to stdout.  Can print only the positive scores (`-p`) and the tweets in addition to score (`-t`).

# `term_sentiment.py`

## About

Generates a sentiment score for words not found in the sentiment dictionary.  A score is generated for each tweet using the method described in `tweet_sentiment.py`.  This score is recorded for each word not found in the dictionary.  Once all tweets are read from stdin the average for each new word is computed and printed to stdout.

## Usage

Running `./term_sentiment.py` requires twitter data (in json format) in stdin.  This can be pipped with `twitterstream.py` or run using saved data.  New words and scores are printed to stdout, tab-separated.

# `happiest_state.py`

## About

Determines the happiest state from the tweets read.  Tweets are scored using the method describe in `tweet_sentiment.py`.  The location is determined from the "place":"full_name" attribute of the JSON data.  Tweets missing this information are ignored.  The two letter abbreivation for the state with the highest average score is printed to stdout.


# `frequency.py`

## About

Determiens the frequency of different words found in tweets.  The frequency is measured simply as a count.  The word and frequeyc is printed to stdout.

## Usage

Running `./frequency.py` requires twitter data (in json format) in stdin.  This can be pipped with `twitterstream.py` or run using saved data.


# `top_ten.py`

## About

Determines the top ten hash tags and prints them to stdout with their count.

## Usage

Running `./top_ten.py` requires twitter data (in json format) in stdin.  This can be pipped with `twitterstream.py` or run using saved data.

# Future Work

## Genearl
* Clean tweets (i.e. remove commas so "this," and "this" are the same). Use RegEx?

## `tweet_sentiment`
* Find way to include modifiers (i.e. 'happy' versus 'not happy')

## `term _sentiment.py`
* More advanced learning algorithm to classify words.

# `happiest_state.py`
* Give option for more advanced location classification.  Perhaps an on-line service to look up location from GPS coordinates. Keep current method in place (as no internet required).
* Add option to print happiest state, or list of all states and scores

# `frequency.py`
* Add normlization option (to argparse)
* Add Top Ten (or top n) option
* Add sorting options.
* Add English only option

# `top_ten.py`
* Add English only option