#########################################################################################
# Question 1: Create an app that will be executed in terminal or from the command
# line. The app should accept a hashtag as an argument and should only print out 
# unique urls found in the 100 most recent tweets that matched the hashtag.  
#
# Solution Approach : This question is solved using twitter_text library which 
# gives entities from a twitter text. This program first takes a hash tag from the
# user by command prompt and then using the same searches first 100 recent tweets and 
# stores into a list . This is then operated on extractor class to get urls. The given
# list of urls are not unique which will be stored again into a set which gives a unique 
# set of urls.
##########################################################################################


# importing twitter libraries 
# twitter_text library is used for auto-converting URLs, 
# mentions, hashtags, lists, etc. in Twitter text. 

import twitter
import json
import sys
import twitter_text

# declaring all the variables

list_of_urls_in_tweets = []       # Variable to store list of unique tweets
i=1                               # Counter for printing
search_results = []               # Variable to store the twitter search respons
tweet_text = []                   # Variable to store the tweets

# take hash tag term from command prompt

term = sys.argv[1]

# create twitter API object

twitter_search = twitter.Twitter(domain="search.twitter.com")


# perform a basic search 
# twitter API docs: https://dev.twitter.com/docs/api/1/get/search
# Search arguments shows that the fetches 100 recent tweets of the topic 

search_results=twitter_search.search(q=term, count=100, rpp=100, result_type='recent', include_entities=1)                                               

# Storing all the tweets and making a twitter_text class 

for text in search_results['results']:
  tweet_text.append(text['text'])       

extractor = twitter_text.Extractor(tweet_text) 	

# Getting urls from the tweet text object 

for url in extractor.extract_urls():
  list_of_urls_in_tweets.append(url)
  
# Storing in a set to store unique urls

list_of_urls_in_tweets=list(set(list_of_urls_in_tweets))                                 

for url in list_of_urls_in_tweets:
 print " Url %i : " % i,str(url)
 i+=1

print "Total number of tweets : ",len(search_results['results'])
print "Total number of list_of_urls_in_tweets : ",len(extractor.extract_urls())
print "Total number of unique list_of_urls_in_tweets : ",len(list_of_urls_in_tweets)
