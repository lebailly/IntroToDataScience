# Description

These programs collect current information from twitter and preform different types of basic analysis (such as listing the top hash tags and determining a numeric rating of the tweet sentiment). This project started as part of a Coursera course on [Data Science][1], however I have expanded upon it in several ways.  The original assignment description is available [here][2].

# `twitterstream.py`

## About

Used to fetch live stream data from twitter.  

## Set Up

Requires oauth2.  Must create a file name `login.txt` which contains the api key, the api secret, the token key, and the token secret.  See `login_example.txt' for the format.  To get credentials:

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

Running `./twitterstream.py` will fetch a twitter stream and print the stream (in JSON format) to stdout for 1 minute.  Use `-t` to specify the run time or use `-u` to run for an unlimited length of time.

# `tweet_sentiment.py`

## About

Creates a numeric score rating if the tweet has a positive or negative sentiment.  This is done by using a dictionary which assigns numeric scores to individual words.  The score given to the tweet is the sum of the scores of the words (words not found in the dictionary are scored zero).

## Usage

Running `./tweet_sentiment.py` requires twitter data (in JSON format) in stdin.  This can be pipped with `twitterstream.py` or run using saved data.  Prints the scores to stdout.  Can print only the positive scores (`-p`) and the tweets in addition to score (`-t`).

## Future Work

* Clean tweets (i.e. remove commas so "this," and "this" are the same). Use RegEx?
* Find way to include modifiers (i.e. 'happy' versus 'not happy')


# `term_sentiment.py`

## About

Generates a sentiment score for words not found in the sentiment dictionary.  A score is generated for each tweet using the method described in `tweet_sentiment.py`.  This score is recorded for each word not found in the dictionary.  Once all tweets are read from stdin the average for each new word is computed and printed to stdout.

## Usage

Running `./term_sentiment.py` requires twitter data (in JSON format) in stdin.  This can be pipped with `twitterstream.py` or run using saved data.  New words and scores are printed to stdout, tab-separated.

## Future Work

* More advanced learning algorithm to classify words.

# `happiest_state.py`

## About

Determines the happiest state from the tweets read.  Tweets are scored using the method describe in `tweet_sentiment.py`.  The location is determined from the "place":"full_name" attribute of the JSON data.  Tweets missing this information are ignored.  The two letter abbreviation for the state with the highest average score is printed to stdout.

## Usage

Running `./happiest_state.py` requires twitter data (in JSON format) in stdin.  This can be pipped with `twitterstream.py` or run using saved data.

## Future Work

* Give option for more advanced location classification.  Perhaps an on-line service to look up location from GPS coordinates. Keep current method in place (as no Internet required).
* Add option to print happiest state, or list of all states and scores

# `frequency.py`

## About

Determines the frequency of different words found in tweets.  The frequency is measured simply as a count.  The word and frequency is printed to stdout.

## Usage

Running `./frequency.py` requires twitter data (in JSON format) in stdin.  This can be pipped with `twitterstream.py` or run using saved data.

## Future Work

* Add normalization option to argparse
* Add Top Ten (or top n) option
* Add sorting options.
* Add English only option

# `top_ten.py`

## About

Determines the top ten hash tags of the data read from stdin and prints them to stdout with their count.

## Usage

Running `./top_ten.py` requires twitter data (in JSON format) in stdin.  This can be pipped with `twitterstream.py` or run using saved data.

## Future Work

* Add English only option

[1]: https://github.com/uwescience/datasci_course_materials
[2]: https://github.com/lebailly/IntroToDataScience/blob/master/assignment1/assignment1.md