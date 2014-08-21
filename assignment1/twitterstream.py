#!/usr/bin/env python2.7

"""
Program streams tweets from JSON source specified by --url.  Stream is read
for -t minutes. Log-in information in the form

api_key <api key>
api_secret <api secret>
token_key <token key>
token_secret <token secret>

is read from --login. Twitter data, in JSON format, is outputted to stdout.

This program was originally developed by Bill Howe (used as part of the
"Introduction to Data Science" course on Coursera).  I altered the program to
output the data to stdout (not a file, so it could be part of a pipe) and also 
added all the argparse options (which removed the requirement of hardwiring
the twitter credentials, along with add the timing features).
"""

import oauth2 as oauth
import urllib2 as urllib
import argparse, sys
from time import time

def main():
  """
  Parses arguments, retrieves twitter stream, outputs stream in JSON format.
  """

  options = parse_arguments()

  login = {}
  for line in options.login:
    key, value = line.split()
    login[key] = value

  response = twitterreq(url = options.url,login = login, 
    method = "GET", debug = options.debug)

  stop = time() + options.run_time*60
  for line in response:
    if(time() > stop and not options.unlimited): break
    print line.strip()

def twitterreq(url, login, method = 'GET', parameters = [], debug = 0):
  """
  Reads log in information from stdin.
  Construct, sign, and open a twitter request using this information.
  """

  oauth_token=oauth.Token(key=login['access_token'],secret=login['token_secret'])
  oauth_consumer=oauth.Consumer(key=login['api_key'],secret=login['api_secret'])

  signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

  http_handler  = urllib.HTTPHandler(debuglevel=debug)
  https_handler = urllib.HTTPSHandler(debuglevel=debug)

  req = oauth.Request.from_consumer_and_token(oauth_consumer,
        token=oauth_token, http_method=method, 
        http_url=url, parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if method == "POST": encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def parse_arguments():
    """ Parses arguments from command line."""

    parser = argparse.ArgumentParser(description = __doc__)

    parser.add_argument('--login', '-l', type=argparse.FileType('r'), 
      nargs='?', default='login.txt',
      help='''Log-in info in a text file containing the following information:
                api_key <api key> \\n
                api_secret <api secret> \\n
                token_key <token key> \\n
                token_secret <token secret>. Defaults to 'login.txt' ''')
    parser.add_argument('--run_time', '-t', type=float, default=1,
        help="Length of time (in minutes) to collect data from twitter stream.")
    parser.add_argument('--unlimited', '-u', action='store_true',default=False,
        help="Stream data with no time limit (defaults to False).")  
    parser.add_argument('--url', type=str, 
      default="https://stream.twitter.com/1/statuses/sample.json",
      help='''URL location of JSON data source.  Defaults to 
              https://stream.twitter.com/1/statuses/sample.json''')
    parser.add_argument('--debug', '-d', type=str, default=0,
      help="Debug for urllib.HTTPHandler and urlib.HTTPSHandler (default 0).")
    parser.add_argument('--method', '-m', type=str, default='GET',
      help='''http_method used in oauth.Request.from_consumer_and_token 
      (default is 'GET').''')

    return parser.parse_args()

if __name__ == '__main__':
  main()
