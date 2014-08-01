#!/usr/bin/env python2.7

"""
Program streams tweets from json source specified by --url.  Stream is read
for -t minutes. Log-in information in the form

api_key <api key>
api_secret <api secret>
token_key <token key>
token_secret <token secret>

is read from stdin. Twitter data, in json format, is outputted to stdout.
"""

import oauth2 as oauth
import urllib2 as urllib
import argparse, sys
from time import time

def main():
  """
  Parses arguments, retrives twitter stream, outputs
  """

  options = parse_arguments()

  log_in = {}
  for line in options.log_in:
    key, value = line.split()
    log_in[key] = value

  response = twitterreq(url = options.url,log_in = log_in, 
    method = "GET", debug = options.debug)

  stop = time() + options.run_time*60
  for line in response:
    if(time() > stop): break
    print line.strip()

def twitterreq(url, log_in, method = 'GET', parameters = [], debug = 0):
  """
  Reads log in information from stdin.
  Construct, sign, and open a twitter request using this information.
  """

  oauth_token=oauth.Token(key=log_in['access_token'],secret=log_in['token_secret'])
  oauth_consumer=oauth.Consumer(key=log_in['api_key'],secret=log_in['api_secret'])

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
    """ Parses arguments from comandline."""

    parser = argparse.ArgumentParser(description = __doc__)

    parser.add_argument('--log_in', '-l', type=argparse.FileType('r'), 
      nargs='?', default='login.txt',
      help='''Log-in info in a text file containg the following informaiton:
                api_key <api key> \\n
                api_secret <api secret> \\n
                token_key <token key> \\n
                token_secret <token secret>. Defaults to 'login.txt' ''')
    parser.add_argument('--run_time', '-t', type=float, default=1,
        help="Lenght of time (in minutes) to collect data from twitter stream.")  
    parser.add_argument('--url', '-u', type=str, 
      default="https://stream.twitter.com/1/statuses/sample.json",
      help='''URL location of json data source.  Defaults to 
              https://stream.twitter.com/1/statuses/sample.json''')
    parser.add_argument('--debug', '-d', type=str, default=0,
      help="Debug for urllib.HTTPHandler and urlib.HTTPSHandler (default 0).")
    parser.add_argument('--method', '-m', type=str, default='GET',
      help='''http_method used in oauth.Request.from_consumer_and_token 
      (default is 'GET').''')

    return parser.parse_args()

if __name__ == '__main__':
  main()
