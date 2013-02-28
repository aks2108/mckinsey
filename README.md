This repository is intended to create and publish my assignments required by Mckinsey. The set of questions that I have been given are:

1. Create an app that will be executed in terminal or from the command line. The app should accept a hashtag as an argument and should only print out unique urls found in the 100 most recent tweets that matched the hashtag.

2. Given an array of integers, write some code to find all the integers that appear more than once in the array, sorted by which appears most often to least often (once)

The programming language used is  Python.

Detailed description
------------------------------------------------------------------------------------------------------------------
Program 1 : 

This question is solved using by two approaches 
1. Using twitter_text library which gives entities from a twitter text 'extractor.extract_urls()'
2. Using Regular expression operations
This program first takes a hash tag from the user by command prompt and then using the same, searches first 100 recent tweets and stores into a list . Then the text of the tweets is operated on the 'findall' function corrosponding to a pattern which peculiar to urls which gives a list of urls present in the tweets. The list of urls stored again into a set which gives a unique  set of urls.

Key properties :

1. Used regular expression class 're'
2. The pattern used is ('(https?://\S+)', text['text']) which means all the terms starting with https:// and make sure the terms in url are not matched further in the text if present
3. Unique urls has been derived by putting the duplicate set of list into a set which takes unique values.
4. The performance of the application is of the order O(n) and it is fast to process.

Assumptions :

1. The urls starts with http:// and https://
2. Only tweets urls have been processed
3. List of unique urls have been displayed not all
4. No media item or elongated urls are required

Output :

C:\Python27>python question_1__list_of_urls_tweets.py #budget

 Url 1 :  http://t.co/TFg6M7I5XD',
 Url 2 :  http://t.co/tOF4rOlqn7',
 Url 3 :  http://t.co/9rVfxcbW7L
 Url 4 :  http://t.co/qnJNrq5Dme',
 Url 5 :  http://t.co/FhNMMfLIo3
 Url 6 :  http://t.co/3No0sUU8px',
 Url 7 :  http://t.co/nvEkQ3yqCd',
 Url 8 :  http://t.co/0UlQz7nggO',
 Url 9 :  http://t.co/EK4tJ3O6Kk
 Url 10 :  http://t.co/PDAjSmqKMC',
 Url 11 :  http://t.co/9ZrX08713u',
 Url 12 :  http://t.co/rBmtsPCLTm
 
 Total number of tweets :  100
 
 Total number of list_of_urls_in_tweets :  14 
 
 Total number of unique list_of_urls_in_tweets :  12

-------------------------------------------------------------------------------------------------------
Program 2 : 

Used Counter function of the collection class A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values.

Key Properties :

1. Fast and simple uses counter function of collection class.
2. Takes values from the user and follow the following test cases :
  - One can enter only an array of integers
  - An empty array will throw error
  - A string element in the array will throw error
3. Display elements with frequency in a sorted order

Assumptions :

1. The code displays elements with thier frequencies to facilitate better decision making
2. The user is asked to enter an array of integers everything else will throw error
3. Counter class is used from collection class.

Output :


C:\Python27>python question_2__array_frequency.py

Please enter an array of integers in the form (ex:[2,3,5,3]) :[1,2,22,45,3,5,5,5]

Elements with frequencies highest to lowest are: [(5, 3), (1, 1), (2, 1), (3, 1), (45, 1), (22, 1)]

